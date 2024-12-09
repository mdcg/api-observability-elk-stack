from tests.integration.application.api.routers.task_router.task_router_fixtures import TaskRouterFixtures


class TestUpdateTask(TaskRouterFixtures):
    def test_should_update_task_successfully(self, client, task_model):
        response = client.put(f"/tasks/{task_model.id}")
        assert response.status_code == 200

        response_payload = response.json()

        response_payload["id"] = task_model.id
        response_payload["title"] = task_model.title
        response_payload["description"] = task_model.description
        response_payload["is_completed"] = not task_model.is_completed

    def test_should_return_not_found_if_task_doesnt_exist(self, client, task):
        response = client.put(f"/tasks/{task.id}")
        assert response.status_code == 404
