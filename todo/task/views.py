from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import ListView, CreateView, FormView, RedirectView

from .models import Todo
from .forms import TodoForm, CreateUserForm


class TodoCountMixin(object):
    def get_queryset(self):
        return Todo.objects.filter(author=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list'] = Todo.objects.filter(author=self.request.user).count()
        context['overtime'] = Todo.objects.filter(author=self.request.user, deadline__lt=datetime.now()).count()
        context['important'] = Todo.objects.filter(author=self.request.user, priority='1').count()
        context['normal'] = Todo.objects.filter(author=self.request.user, priority='2').count()
        context['minor'] = Todo.objects.filter(author=self.request.user, priority='3').count()
        return context


class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('task:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list'] = '　'
        context['overtime'] = '　'
        return context


class LoginView(FormView):
    template_name = 'registration/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('task:list')

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list'] = '　'
        context['overtime'] = '　'
        return context


class LogoutView(RedirectView):
    url = ''
    pattern_name = 'task:list'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class TaskCreateView(TodoCountMixin, CreateView):
    template_name = 'task/todo_create.html'
    form_class = TodoForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('task:list')


class TaskListView(TodoCountMixin, ListView):
    template_name = 'task/todo_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return Todo.objects.filter(author=self.request.user)


class TaskTimeoutListView(TodoCountMixin, ListView):
    template_name = 'task/todo_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskTimeoutListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return Todo.objects.filter(author=self.request.user, deadline__lt=datetime.now())


class TaskImportantListView(TodoCountMixin, ListView):
    template_name = 'task/todo_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskImportantListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return Todo.objects.filter(author=self.request.user, priority='1')


class TaskNormalListView(TodoCountMixin, ListView):
    template_name = 'task/todo_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskNormalListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return Todo.objects.filter(author=self.request.user, priority='2')


class TaskMinorListView(TodoCountMixin, ListView):
    template_name = 'task/todo_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskMinorListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return Todo.objects.filter(author=self.request.user, priority='3')


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
