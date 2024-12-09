from unittest.mock import Mock

from pytest import fixture

from task_service.infrastructure.repositories.task_repository import TaskRepository
from tests.factories.task_factory import TaskFactory


class DeleteTaskUseCaseFixtures:
    @fixture
    def task_repository(self):
        return Mock(spec=TaskRepository)

    @fixture
    def task(self):
        return TaskFactory.create()
