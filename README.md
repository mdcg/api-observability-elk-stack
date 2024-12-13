# api-observability-elk-stack

```
export $(cat .env | xargs)
uvicorn task_service.application.api:app --host 0.0.0.0 --port 8000 --reload
```


Elastic Search CA Troubleshooting
```
docker cp api-observability-elk-stack-es01-1:/usr/share/elasticsearch/config/certs/ca/ca.crt /tmp/.

curl --cacert /tmp/ca.crt -u elastic:changeme https://localhost:9200
```
