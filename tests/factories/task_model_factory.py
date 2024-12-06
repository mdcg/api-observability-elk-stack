from factory import Faker

from tests.factories import DbModelFactory
from task_service.infrastructure.database.models.task_model import TaskModel


class TaskModelFactory(DbModelFactory):
    class Meta:
        model = TaskModel

    title = Faker("word")
    description = Faker("paragraph", nb_sentences=2)
    is_completed = Faker("pybool")
