from tests.integration.application.api.routers.task_router.task_router_fixtures import TaskRouterFixtures


class TestDeleteTask(TaskRouterFixtures):
    def test_should_delete_task_successfully(self, client, task_model):
        task_id = task_model.id

        response = client.delete(f"/tasks/{task_id}")
        assert response.status_code == 200

        response_payload = response.json()

        response_payload["id"] = task_id
        response_payload["title"] = task_model.title
        response_payload["description"] = task_model.description
        response_payload["is_completed"] = not task_model.is_completed

        response = client.get(f"/tasks/{task_id}")
        assert response.status_code == 404
