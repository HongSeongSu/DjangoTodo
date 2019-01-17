from django.urls import path
from .views import TaskView, TaskCreateView, TaskListView, TaskTimeoutListView, task_complete, task_delete

app_name = 'task'
urlpatterns = [
    path('create/', TaskCreateView.as_view(), name='create'),
    path('complete/<int:id>/', task_complete, name='complete'),
    path('list/', TaskListView.as_view(), name='list'),
    path('timeout/', TaskTimeoutListView.as_view(), name='timeout'),
    path('delete/<int:id>/', task_delete, name='delete'),
    # path('', TaskView.as_view(), name='todo'),
]
