from django.urls import path
from .views import TaskCreateView, TaskListView, TaskTimeoutListView, task_complete
from .views import TaskView

app_name = 'task'
urlpatterns = [
    path('create/', TaskCreateView.as_view(), name='create'),
    path('complete/<int:id>/', task_complete, name='complete'),
    path('list/', TaskListView.as_view(), name='list'),
    path('timeout/', TaskTimeoutListView.as_view(), name='timeout'),
    path('', TaskView.as_view(), name='todo'),
]
