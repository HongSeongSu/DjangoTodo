from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView

from .models import Todo
from .forms import TodoForm


class TaskCreateView(CreateView):
    template_name = 'task/todo_create.html'
    form_class = TodoForm
    queryset = Todo.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('task:list')


class TaskListView(ListView):
    template_name = 'task/todo_list.html'
    queryset = Todo.objects.all()


class TaskTimeoutListView(ListView):
    template_name = 'task/todo_timeout.html'
    queryset = Todo.objects.all()


def task_complete(request, id):
    task = Todo.objects.get(id=id)
    if task.completed:
        task.completed = 0
    else:
        task.completed = 1
    task.save()
    if request.META.get('HTTP_REFERER')[-5:-1] == 'list':
        return redirect('task:list')
    elif request.META.get('HTTP_REFERER')[-8:-1] == 'timeout':
        return redirect('task:timeout')


def task_delete(request, id):
    Todo.objects.filter(id=id).delete()

    if request.META.get('HTTP_REFERER')[-5:-1] == 'list':
        return redirect('task:list')
    elif request.META.get('HTTP_REFERER')[-8:-1] == 'timeout':
        return redirect('task:timeout')
