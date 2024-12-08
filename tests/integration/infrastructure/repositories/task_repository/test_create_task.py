from task_service.domain.entities.task import Task
from task_service.infrastructure.database.models.task_model import TaskModel
from task_service.infrastructure.repositories.task_repository import TaskRepository
from tests.integration.infrastructure.repositories.task_repository.task_repository_fixtures import (
    TaskRepositoryFixtures,
)


class TestCreateTask(TaskRepositoryFixtures):
    def test_repository_should_create_task_successfully(self, session, task_payload):
        repository = TaskRepository(session)
        task = repository.create_task(
            title=task_payload["title"],
            description=task_payload["description"],
        )

        assert isinstance(task, Task)
        assert task.title == task_payload["title"]
        assert task.description == task_payload["description"]
        assert not task.is_completed
