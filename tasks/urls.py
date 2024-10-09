from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.taskList, name='task-list'),
    path('tasks/<int:pk>/', views.taskDetail, name='task-detail'),
]