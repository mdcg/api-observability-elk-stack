from task_service.infrastructure.database.models.task_model import TaskModel
from task_service.infrastructure.repositories.task_repository import TaskRepository
from tests.integration.infrastructure.repositories.task_repository.task_repository_fixtures import (
    TaskRepositoryFixtures,
)


class TestDeleteTask(TaskRepositoryFixtures):
    def test_repository_should_delete_task_successfully(self, session, task_model):
        repository = TaskRepository(session)
        assert len(repository.get_tasks()) == 1

        repository.delete_task(task_id=task_model.id)
        assert len(repository.get_tasks()) == 0

    def test_repository_should_return_none_if_task_doesnt_exist(self, session):
        repository = TaskRepository(session)
        task = repository.delete_task(task_id=999)
        assert task is None
