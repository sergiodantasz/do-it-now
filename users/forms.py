from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from utils.forms import validate_password, make_error_messages, set_attribute, set_placeholder


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        set_placeholder(self.fields.get('username'), 'Enter your username')
        set_placeholder(self.fields.get('first_name'), 'Enter your first name')
        set_placeholder(self.fields.get('last_name'), 'Enter your last name')
        set_placeholder(self.fields.get('password'), 'Enter your password')
        set_placeholder(self.fields.get('confirm_password'), 'Confirm your password')
        set_attribute(self.fields.get('username'), 'autofocus', True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']

    username = forms.CharField(
        label='Username',
        required=True,
        min_length=5,
        max_length=150,
        error_messages=make_error_messages(field='username', min_length=5, max_length=150),
    )
    first_name = forms.CharField(
        label='First name',
        required=True,
        min_length=1,
        max_length=150,
        error_messages=make_error_messages(['unique'], field='first_name', min_length=1, max_length=150),
    )
    last_name = forms.CharField(
        label='Last name',
        required=True,
        min_length=1,
        max_length=150,
        error_messages=make_error_messages(['unique'], field='last_name', min_length=1, max_length=150),
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
        required=True,
        min_length=8,
        error_messages=make_error_messages(['unique', 'max_length'], field='password', min_length=8),
        validators=[validate_password],
    )
    confirm_password = forms.CharField(
        label='Password (again)',
        widget=forms.PasswordInput(),
        required=True,
        min_length=8,
        error_messages=make_error_messages(['unique', 'max_length'], field='password', min_length=8),
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if confirm_password != password:
            raise ValidationError('The passwords do not match.', code='invalid')
        return confirm_password


class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        set_placeholder(self.fields.get('username'), 'Username')
        set_placeholder(self.fields.get('password'), 'Password')
        set_attribute(self.fields.get('username'), 'autofocus', True)

    username = forms.CharField(
        label='Username',
        required=True,
        min_length=5,
        max_length=150,
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
        required=True,
        min_length=8,
    )
