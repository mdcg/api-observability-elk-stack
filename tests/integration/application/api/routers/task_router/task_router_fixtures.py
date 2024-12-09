from pytest import fixture

from tests.factories.task_factory import TaskFactory
from tests.factories.task_model_factory import TaskModelFactory


class TaskRouterFixtures:
    @fixture
    def task(self):
        return TaskFactory.create()

    @fixture
    def task_model(self):
        return TaskModelFactory.create()

    @fixture
    def task_model_batch(self):
        return TaskModelFactory.create_batch(size=10)
