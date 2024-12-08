from task_service.domain.entities.task import Task
from task_service.infrastructure.repositories.task_repository import TaskRepository


class CreateTaskUseCase:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def save(self, task: Task):
        return self.task_repository.create_task(title=task.title, description=task.description)
