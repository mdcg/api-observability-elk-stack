from task_service.infrastructure.database.models.task_model import TaskModel
from task_service.infrastructure.repositories.task_repository import TaskRepository
from tests.integration.infrastructure.repositories.task_repository.task_repository_fixtures import (
    TaskRepositoryFixtures,
)


class TestUpdateTaskStatus(TaskRepositoryFixtures):
    def test_repository_should_update_task_successfully(self, session, task_model):
        repository = TaskRepository(session)
        assert task_model.is_completed is False

        task = repository.update_task_status(task_id=task_model.id, is_completed=True)

        assert task_model.id == task.id
        assert task.is_completed is True
