from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from task_service.domain.entities.task import Task
from task_service.domain.use_cases.create_task_use_case import CreateTaskUseCase
from task_service.infrastructure.database.connection import session
from task_service.infrastructure.repositories.task_repository import TaskRepository

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=dict)
async def create_task(task: Task, db: Session = Depends(session)):
    task_repository = TaskRepository(db)
    task = CreateTaskUseCase(task_repository).save(task)
    return {"message": "Tarefa criada com sucesso!", "task": task}


@router.get("/", response_model=list)
async def read_tasks(db: Session = Depends(session)):
    tasks = TaskRepository(db).get_tasks()
    return tasks


@router.get("/{task_id}", response_model=dict)
async def read_task(task_id: int, db: Session = Depends(session)):
    task = TaskRepository(db).get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return {"task": task}


@router.put("/{task_id}", response_model=dict)
async def update_task(
    task_id: int, title: str = None, description: str = None, is_completed: bool = None, db: Session = Depends(session)
):
    task = TaskRepository(db).update_task(
        task_id=task_id, title=title, description=description, is_completed=is_completed
    )
    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return {"message": "Tarefa atualizada com sucesso!", "task": task}


@router.delete("/{task_id}", response_model=dict)
async def delete_task(task_id: int, db: Session = Depends(session)):
    task_repository = TaskRepository(db)
    task = task_repository.get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    task_repository.delete_task(task_id)
    return {"message": "Tarefa excluída com sucesso!"}
