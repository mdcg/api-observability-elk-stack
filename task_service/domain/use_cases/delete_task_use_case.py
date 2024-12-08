from task_service.domain.entities.task import Task
from task_service.infrastructure.repositories.task_repository import TaskRepository


class DeleteTaskUseCase:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def delete(self, task_id):
        return self.task_repository.delete_task(task_id)
