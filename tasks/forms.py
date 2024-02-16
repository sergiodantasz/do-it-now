from django import forms

from tasks.models import Task
from utils.forms import make_error_messages, set_attribute, set_placeholder


class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        set_placeholder(self.fields.get('name'), 'Arrange the bookshelf...')
        set_attribute(self.fields.get('name'), 'autofocus', True)

    class Meta:
        model = Task
        fields = ['name']

    name = forms.CharField(
        label='Name',
        required=True,
        min_length=1,
        max_length=250,
        error_messages=make_error_messages(field='task', min_length=1, max_length=250),
    )
