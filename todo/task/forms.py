from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

from .models import Todo, PRIORITY


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'note', 'deadline', 'priority']

    title = forms.CharField(
        label='할 일',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '무엇을 할까',
                'id': 'title',
            }
        )
    )

    note = forms.CharField(
        label='자세한 내용',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '자세한 내용',
            }
        )
    )

    deadline = forms.DateTimeField(
        label='언제까지',
        widget=forms.DateTimeInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    priority = forms.ChoiceField(
        choices=PRIORITY,
        label="중요도",
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )


class CreateUserForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        label='ID',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': ''
            }
        )
    )

    password1 = forms.CharField(
        required=True,
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '문자와 숫자를 포함해 8자리 이상 입력'
            }
        )
    )

    password2 = forms.CharField(
        required=True,
        label='비밀번호 확인',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '같은 비밀번호를 다시 입력'
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
