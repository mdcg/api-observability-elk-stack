from factory import Faker

from task_service.infrastructure.database.models.task_model import TaskModel
from tests.factories import DbModelFactory


class TaskModelFactory(DbModelFactory):
    class Meta:
        model = TaskModel

    title = Faker("word")
    description = Faker("paragraph", nb_sentences=2)
    is_completed = Faker("pybool")
