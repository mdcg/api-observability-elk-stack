# api-observability-elk-stack

```
export $(cat .env | xargs)
uvicorn task_service.application.api:app --host 0.0.0.0 --port 8000 --reload
```
