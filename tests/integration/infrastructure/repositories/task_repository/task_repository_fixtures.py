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
    def task(self):
        return TaskModelFactory.create(is_completed=False)
