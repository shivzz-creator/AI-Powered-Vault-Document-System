from celery import Celery

celery_app = Celery(
    "aivault",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)

# 🔴 FORCE IMPORT (this registers the task)
import app.workers.ingestion  # noqa
