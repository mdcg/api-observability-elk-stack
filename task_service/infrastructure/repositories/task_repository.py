from sqlalchemy.orm import Session

from task_service.infrastructure.database.models.task_model import TaskModel
from task_service.infrastructure.repositories.exceptions import TaskNotFoundError


class TaskRepository:
    def __init__(self, session: Session):
        self.session = session

    def __get_task_model_by_id(self, task_id: int):
        task = self.session.get(TaskModel, task_id)
        if not task:
            raise TaskNotFoundError(task_id)

        return task

    def create_task(self, title: str, description: str = None):
        task = TaskModel(title=title, description=description)
        self.session.add(task)
        self.session.flush()
        self.session.refresh(task)

        return task.to_entity()

    def get_tasks(self):
        return [task_model.to_entity() for task_model in self.session.query(TaskModel).all()]

    def get_task_by_id(self, task_id: int):
        try:
            task = self.__get_task_model_by_id(task_id)
        except TaskNotFoundError:
            return None

        return task.to_entity()

    def update_task_status(self, task_id: int):
        try:
            task = self.__get_task_model_by_id(task_id)
        except TaskNotFoundError:
            return None

        task.is_completed = not task.is_completed

        self.session.flush()
        self.session.refresh(task)

        return task.to_entity()

    def delete_task(self, task_id: int):
        try:
            task = self.__get_task_model_by_id(task_id)
        except TaskNotFoundError:
            return None

        self.session.delete(task)
        self.session.flush()

        return task
