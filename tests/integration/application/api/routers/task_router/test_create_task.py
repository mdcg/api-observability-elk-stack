from tests.integration.application.api.routers.task_router.task_router_fixtures import TaskRouterFixtures


class TestCreateTask(TaskRouterFixtures):
    def test_should_create_task_successfully(self, client, task):
        response = client.post("/tasks", json={"title": task.title, "description": task.description})
        assert response.status_code == 200

        response_payload = response.json()

        assert response_payload["title"] == task.title
        assert response_payload["description"] == task.description
        assert response_payload["is_completed"] == False
