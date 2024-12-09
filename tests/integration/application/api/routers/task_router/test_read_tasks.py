from tests.integration.application.api.routers.task_router.task_router_fixtures import TaskRouterFixtures


class TestReadTasks(TaskRouterFixtures):
    def test_should_read_tasks_successfully(self, client, task_model_batch):
        response = client.get("/tasks")
        assert response.status_code == 200

        response_payload = response.json()

        assert len(response_payload) == 10
