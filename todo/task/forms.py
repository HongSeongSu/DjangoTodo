from django import forms
from .models import Todo, PRIORITY


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'note', 'deadline', 'priority']
        # fields = '__all__'
        # widgets = {
        #     'deadline': DatePickerWidget,
        # }

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


# class TodoCompleteForm(forms.ModelForm):
#     class Meta:
#         model = Todo
#         fields = ['completed']
