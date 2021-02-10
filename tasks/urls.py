from django.urls import path 
from tasks.models import Task

from .views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    CompletedTaskView,
)

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('new/', TaskCreateView.as_view(), name='task_create'),
    path('completed/<slug:slug>/', CompletedTaskView.as_view(), name='task_completed'),
    path('edit/<slug:slug>/', TaskUpdateView.as_view(), name='task_update'),
    path('delete/<slug:slug>/', TaskDeleteView.as_view(), name='task_delete'),
]