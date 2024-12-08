from task_service.domain.entities.task import Task
from task_service.infrastructure.repositories.task_repository import TaskRepository


class GetTaskUseCase:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def get(self, task_id: int):
        return self.task_repository.get_task_by_id(task_id)
