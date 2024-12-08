from task_service.domain.entities.task import Task
from task_service.infrastructure.repositories.task_repository import TaskRepository


class ListTasksUseCase:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def list_all(self):
        return self.task_repository.get_tasks()
