# myapp/tasks.py
import logging
from celery import shared_task
from time import sleep

logger = logging.getLogger(__name__)

@shared_task
def send_email_task(to_email, subject, body):
    logger.info(f"Task started: send_email to {to_email}")
    sleep(10)  # Simulation
    logger.info(f"Task completed: send_email to {to_email}")
    return f"Email sent to {to_email} with subject {subject}"

@shared_task
def some_heavy_task(x, y):
    sleep(5)  # Simulation
    return x * y



@shared_task
def periodic_task():
    print("Periodic task running")
