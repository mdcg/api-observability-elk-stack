from task_service.domain.use_cases.create_task_use_case import CreateTaskUseCase
from tests.unit.use_cases.create_task_use_case.create_task_use_case_fixtures import CreateTaskUseCaseFixtures


class TestSave(CreateTaskUseCaseFixtures):
    def test_should_save_task_successfully(self, task_repository, task):
        CreateTaskUseCase(task_repository).save(task)
        task_repository.create_task.assert_called_with(title=task.title, description=task.description)
