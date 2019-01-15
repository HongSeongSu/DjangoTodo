from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, CreateView, TemplateView, RedirectView, FormView, DeleteView
from django.views.generic.detail import SingleObjectMixin

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
    return redirect('task:list')


class TaskListsView(ListView):
    model = Todo
    template_name = 'task/todo.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TodoForm
        return context


class TodoFormView(SingleObjectMixin, FormView):
    template_name = 'task/todo.html'
    form_class = TodoForm
    model = Todo

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('todo', kwargs={'pk': self.object.pk})


class TaskView(View):
    def get(self, request, *args, **kwargs):
        view = TaskListsView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = TodoFormView.as_view()
        return view(request, *args, **kwargs)
