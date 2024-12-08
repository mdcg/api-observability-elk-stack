from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from task_service.domain.entities.task import Task
from task_service.domain.use_cases.create_task_use_case import CreateTaskUseCase
from task_service.domain.use_cases.delete_task_use_case import DeleteTaskUseCase
from task_service.domain.use_cases.get_task_use_case import GetTaskUseCase
from task_service.domain.use_cases.list_tasks_use_case import ListTasksUseCase
from task_service.domain.use_cases.update_task_use_case import UpdateTaskUseCase
from task_service.infrastructure.database.connection import session
from task_service.infrastructure.repositories.task_repository import TaskRepository

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=Task)
async def create_task(task: Task, db: Session = Depends(session)):
    return CreateTaskUseCase(TaskRepository(db)).save(task)


@router.get("/", response_model=list)
async def read_tasks(db: Session = Depends(session)):
    return ListTasksUseCase(TaskRepository(db)).list_all()


@router.get("/{task_id}", response_model=Task)
async def read_task(task_id: int, db: Session = Depends(session)):
    task = GetTaskUseCase(TaskRepository(db)).get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return task


@router.put("/{task_id}", response_model=Task)
async def update_task(task_id: int, db: Session = Depends(session)):
    task = UpdateTaskUseCase(TaskRepository(db)).update(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return task


@router.delete("/{task_id}", response_model=Task)
async def delete_task(task_id: int, db: Session = Depends(session)):
    return DeleteTaskUseCase(TaskRepository(db)).delete(task_id)
