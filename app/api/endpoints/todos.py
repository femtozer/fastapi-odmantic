from typing import Any, List

from fastapi import APIRouter, HTTPException, status
from odmantic import ObjectId

from app.db.engine import engine
from app.models.todos import Todo

router = APIRouter()


@router.get("", response_model=List[Todo])
async def read_todos() -> Any:
    todos = await engine.find(Todo)
    return todos


@router.put("", response_model=Todo)
async def upsert_todo(todo: Todo) -> Any:
    todo = await engine.save(todo)
    return todo


@router.get("/{id}", response_model=Todo)
async def read_todo(id: ObjectId) -> Any:
    todo = await engine.find_one(Todo, Todo.id == id)
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return todo
