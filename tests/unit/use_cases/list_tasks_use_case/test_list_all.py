from task_service.domain.use_cases.list_tasks_use_case import ListTasksUseCase
from tests.unit.use_cases.list_tasks_use_case.list_tasks_use_case_fixtures import ListTasksUseCaseFixtures


class TestList(ListTasksUseCaseFixtures):
    def test_should_list_tasks_successfully(self, task_repository, task):
        ListTasksUseCase(task_repository).list_all()
        task_repository.get_tasks.assert_called_with()
