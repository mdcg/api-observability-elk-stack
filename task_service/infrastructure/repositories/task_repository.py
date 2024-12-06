from sqlalchemy.orm import Session
from task_service.infrastructure.database.models.task_model import TaskModel


class TaskRepository:
    def __init__(self, session: Session):
        self.session = session 

    def create_task(self, title: str, description: str = None):
        task = TaskModel(title=title, description=description)
        self.session.add(task)
        self.session.flush()
        self.session.refresh(task)

        return task

    def get_tasks(self):
        return self.session.query(TaskModel).all()

    def get_task_by_id(self, task_id: int):
        return self.session.query(TaskModel).filter(TaskModel.id == task_id).first()

    def update_task_status(self, task_id: int, is_completed: bool):
        task = self.get_task_by_id(task_id)
        if task:
            task.is_completed = is_completed
            self.session.flush()
            self.session.refresh(task)

        return task

    def delete_task(self, task_id: int):
        task = self.get_task_by_id(task_id)
        if task:
            self.session.delete(task)
            self.session.flush()

        return task
