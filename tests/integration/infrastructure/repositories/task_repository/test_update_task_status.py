from task_service.infrastructure.database.models.task_model import TaskModel
from task_service.infrastructure.repositories.task_repository import TaskRepository
from tests.integration.infrastructure.repositories.task_repository.task_repository_fixtures import (
    TaskRepositoryFixtures,
)


class TestUpdateTaskStatus(TaskRepositoryFixtures):
    def test_repository_should_update_task_successfully(self, session, task_model):
        repository = TaskRepository(session)
        assert task_model.is_completed is False

        task = repository.update_task_status(task_id=task_model.id)

        assert task_model.id == task.id
        assert task.is_completed is True

    def test_repository_should_return_none_if_task_doesnt_exist(self, session):
        repository = TaskRepository(session)
        task = repository.update_task_status(task_id=999)
        assert task is None
