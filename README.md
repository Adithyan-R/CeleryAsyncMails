celery.py sets up Celery and configures it to use the settings from Django.

tasks.py defines tasks including a periodic task, an email-sending task, and a heavy computation task.

views.py defines views to submit tasks asynchronously and to check the status and result of these tasks using the task ID.

views.py defines views to submit tasks asynchronously and to check the status and result of these tasks using the task ID.

success.html will displays the task ID after the task is submitted.

result.html will displays the task result when checked.
