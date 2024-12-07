from pytest import fixture

from tests.factories.task_model_factory import TaskModelFactory


class TaskRepositoryFixtures:
    @fixture
    def task_payload(self):
        return {
            "title": "Lorem Ipsum",
            "description": "Lorem ipsum dolor sit amet",
        }

    @fixture
    def task_model(self):
        return TaskModelFactory.create(is_completed=False)

    @fixture
    def task_model_batch(self):
        return TaskModelFactory.create_batch(size=10, is_completed=False)
