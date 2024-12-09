from task_service.domain.use_cases.delete_task_use_case import DeleteTaskUseCase
from tests.unit.use_cases.delete_task_use_case.delete_task_use_case_fixtures import DeleteTaskUseCaseFixtures


class TestDelete(DeleteTaskUseCaseFixtures):
    def test_should_delete_task_successfully(self, task_repository, task):
        DeleteTaskUseCase(task_repository).delete(task.id)
        task_repository.delete_task.assert_called_with(task.id)
