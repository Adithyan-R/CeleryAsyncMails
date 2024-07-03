# Create your views here.

from django.shortcuts import render
from .tasks import send_email_task, some_heavy_task
from celery.result import AsyncResult

def send_email_view(request):
    to_email = request.GET.get('to_email', 'example@example.com')
    subject = request.GET.get('subject', 'Hello')
    body = request.GET.get('body', 'This is a test email.')
    result = send_email_task.delay(to_email, subject, body)
    return render(request, 'success.html', {'task_id': result})


def check_email_task_view(request, task_id):
    task = AsyncResult(task_id)
    if task.state == 'PENDING':
        result = 'Pending...'
    elif task.state == 'FAILURE':
        result = 'Task failed'
    else:
        result = task.result
    return render(request, 'result.html', {'task_id': task.id, 'result': result})
def heavy_task_view(request):
    result = some_heavy_task.delay(3,4)
    return render(request, 'success.html', {'task_id': result})

def check_heavy_task_view(request, task_id):
    task = AsyncResult(task_id)
    if task.state == 'PENDING':
        result = 'Pending...'
    elif task.state == 'FAILURE':
        result = 'Task failed'
    else:
        result = task.result
    return render(request, 'result.html', {'task_id': task.id, 'result': result})

