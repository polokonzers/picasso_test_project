import logging
from celery import shared_task
from django.db import close_old_connections
from .models import File

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


@shared_task
def small_uploading_handler(file_id):
    logger = logging.getLogger(__name__)
    logger.info(f"Processing file with id {file_id}")


@shared_task
def uploading_handler(file_id):
    close_old_connections()
    logger = logging.getLogger(__name__)
    try:
        file_instance = File.objects.get(pk=file_id)
        file_instance.processed = True
        file_instance.save()
        logger.info(f"File with id {file_id} was processed")
    except File.DoesNotExist:
        logger.error(f"File with id {file_id} not found.")
