from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['title', 'note', 'deadline', 'completed', 'priority']


    title = forms.CharField(
        label='title',
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Enter the title',
                'id': 'title',
            }
        )
    )


