from task_service.domain.entities.task import Task
from task_service.infrastructure.repositories.task_repository import TaskRepository


class UpdateTaskUseCase:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def update(self, task_id):
        return self.task_repository.update_task_status(task_id)
