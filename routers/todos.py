from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database import get_db
from models import Todo
from schemas import TodoCreate, TodoUpdate, TodoOut
from auth import get_current_user
from cache import cache_get, cache_set, cache_delete_pattern
from models import User
from typing import List, Optional

router = APIRouter(prefix="/todos", tags=["todos"])

def _list_key(user_id: int) -> str:
    return f"todos:user:{user_id}"

@router.get("/", response_model=List[TodoOut])
async def list_todos(
    completed: Optional[bool] = None,
    priority: Optional[str] = None,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    cache_key = _list_key(current_user.id)
    cached = await cache_get(cache_key)
    if cached and completed is None and priority is None:
        return cached

    query = select(Todo).where(Todo.user_id == current_user.id).order_by(Todo.created_at.desc())
    if completed is not None:
        query = query.where(Todo.completed == completed)
    if priority:
        query = query.where(Todo.priority == priority)

    result = await db.execute(query)
    todos = result.scalars().all()
    data = [TodoOut.model_validate(t).model_dump() for t in todos]

    if completed is None and priority is None:
        await cache_set(cache_key, data, ttl=120)
    return data

@router.post("/", response_model=TodoOut, status_code=201)
async def create_todo(
    data: TodoCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    todo = Todo(**data.model_dump(), user_id=current_user.id)
    db.add(todo)
    await db.commit()
    await db.refresh(todo)
    await cache_delete_pattern(_list_key(current_user.id))
    return todo

@router.patch("/{todo_id}", response_model=TodoOut)
async def update_todo(
    todo_id: int,
    data: TodoUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(select(Todo).where(Todo.id == todo_id, Todo.user_id == current_user.id))
    todo = result.scalar_one_or_none()
    if not todo:
        raise HTTPException(404, "Todo not found")
    for k, v in data.model_dump(exclude_none=True).items():
        setattr(todo, k, v)
    await db.commit()
    await db.refresh(todo)
    await cache_delete_pattern(_list_key(current_user.id))
    return todo

@router.delete("/{todo_id}", status_code=204)
async def delete_todo(
    todo_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(select(Todo).where(Todo.id == todo_id, Todo.user_id == current_user.id))
    todo = result.scalar_one_or_none()
    if not todo:
        raise HTTPException(404, "Todo not found")
    await db.delete(todo)
    await db.commit()
    await cache_delete_pattern(_list_key(current_user.id))
