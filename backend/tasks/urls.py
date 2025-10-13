from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import task_list, task_detail

router = DefaultRouter()
router.register(r'tasks', task_list, task_detail)

urlpatterns = [
    path('tasks/', task_list, name='task-list'),
    path('tasks/<int:pk>/', task_detail, name='task-detail'),
]
