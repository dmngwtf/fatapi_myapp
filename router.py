from asyncio import tasks
from typing import Annotated
from fastapi import APIRouter, FastAPI
from fastapi import Depends
from repositoty import TaskRepository
from schemas import STaskAdd



router = APIRouter(
    prefix="/tasks"
)


@router.post("")
async def add_task(
    task: Annotated[STaskAdd,Depends()]
):
    task_id = await TaskRepository.add_one(task)
    return {"ok":True, "task_id": task_id}

@router.get("/tasks")
async def get_task():
    tasks = await TaskRepository.find_all()
    return {"data":tasks}

