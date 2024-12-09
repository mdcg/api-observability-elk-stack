import factory
from factory import Faker

from task_service.domain.entities.task import Task


class TaskFactory(factory.Factory):
    class Meta:
        model = Task

    id = Faker("pyint")
    title = Faker("word")
    description = Faker("paragraph", nb_sentences=2)
    is_completed = Faker("pybool")
