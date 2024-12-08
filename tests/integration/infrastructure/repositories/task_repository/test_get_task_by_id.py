from task_service.domain.entities.task import Task
from task_service.infrastructure.database.models.task_model import TaskModel
from task_service.infrastructure.repositories.task_repository import TaskRepository
from tests.integration.infrastructure.repositories.task_repository.task_repository_fixtures import (
    TaskRepositoryFixtures,
)


class TestGetTaskByID(TaskRepositoryFixtures):
    def test_repository_should_get_task_by_id(self, session, task_model):
        repository = TaskRepository(session)
        task = repository.get_task_by_id(task_id=task_model.id)
        assert isinstance(task, Task)

    def test_repository_should_return_none_if_task_doesnt_exist(self, session):
        repository = TaskRepository(session)
        task = repository.get_task_by_id(task_id=999)
        assert task is None
