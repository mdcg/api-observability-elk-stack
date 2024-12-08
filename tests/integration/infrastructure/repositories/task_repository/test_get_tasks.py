from task_service.domain.entities.task import Task
from task_service.infrastructure.database.models.task_model import TaskModel
from task_service.infrastructure.repositories.task_repository import TaskRepository
from tests.integration.infrastructure.repositories.task_repository.task_repository_fixtures import (
    TaskRepositoryFixtures,
)


class TestGetTasks(TaskRepositoryFixtures):
    def test_repository_should_list_all_tasks(self, session, task_model_batch):
        repository = TaskRepository(session)
        tasks = repository.get_tasks()
        assert len(tasks) == 10
        for task in tasks:
            assert isinstance(task, Task)
