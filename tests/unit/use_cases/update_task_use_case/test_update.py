from task_service.domain.use_cases.update_task_use_case import UpdateTaskUseCase
from tests.unit.use_cases.update_task_use_case.update_task_use_case_fixtures import UpdateTaskUseCaseFixtures


class TestUpdate(UpdateTaskUseCaseFixtures):
    def test_should_update_task_successfully(self, task_repository, task):
        UpdateTaskUseCase(task_repository).update(task.id)
        task_repository.update_task_status.assert_called_with(task.id)
