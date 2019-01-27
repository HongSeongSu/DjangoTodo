from django.urls import path
from .views import (
    TaskCreateView, TaskListView, TaskTimeoutListView,
    TaskImportantListView, TaskNormalListView, TaskMinorListView,
    TaskUpdateView, TaskDeleteView)

app_name = 'task'
urlpatterns = [
    path('create/', TaskCreateView.as_view(), name='create'),
    path('complete/<int:id>/', TaskUpdateView.as_view(), name='complete'),
    path('list/', TaskListView.as_view(), name='list'),
    path('timeout/', TaskTimeoutListView.as_view(), name='timeout'),
    path('important/', TaskImportantListView.as_view(), name='important'),
    path('normal/', TaskNormalListView.as_view(), name='normal'),
    path('minor/', TaskMinorListView.as_view(), name='minor'),
    path('delete/<int:id>/', TaskDeleteView.as_view(), name='delete'),
]
