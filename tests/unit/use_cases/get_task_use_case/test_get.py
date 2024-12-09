from task_service.domain.use_cases.get_task_use_case import GetTaskUseCase
from tests.unit.use_cases.get_task_use_case.get_task_use_case_fixtures import GetTaskUseCaseFixtures


class TestGet(GetTaskUseCaseFixtures):
    def test_should_get_task_successfully(self, task_repository, task):
        GetTaskUseCase(task_repository).get(task.id)
        task_repository.get_task_by_id.assert_called_with(task.id)
