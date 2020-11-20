from django.urls import path
from . import views


urlpatterns = [
    path('', views.task_index, name='task_index'),
    path('home/', views.task_index, name='index'),
    path('task/create/', views.TaskCreate.as_view(), name='task_create'),
    path('task/<int:pk>/delete/', views.TaskDelete.as_view(), name='task_delete'),
    path('task/<int:task_id>/', views.task_detail, name='detail'),
]