from celery import Celery
import os

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")

celery_app = Celery(
    "sentinel_worker",
    broker=f"redis://{REDIS_HOST}:{REDIS_PORT}/0",
    backend=f"redis://{REDIS_HOST}:{REDIS_PORT}/1"
)

celery_app.conf.task_routes = {
    "worker.tasks.*": {"queue": "sentinel_queue"}
}