
from django.urls import path
from . import views

urlpatterns = [
    path('send-email/', views.send_email_view, name='send_email'),
    path('check-email/<str:task_id>/', views.check_email_task_view, name='check_email_task'),
    path('heavy-task/', views.heavy_task_view, name='heavy_task'),
    path('check-heavy-task/<str:task_id>/', views.check_heavy_task_view, name='check_heavy_task'),
]
