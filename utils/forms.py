from re import compile
from typing import Any

from django.core.exceptions import ValidationError

ERROR_MESSAGES = {
    'required': 'The {field} is required.',
    'min_length': 'The {field} must have at least {min_length} characters.',
    'max_length': 'The {field} must have a maximum of {max_length} characters.',
    'invalid': 'This {field} is not valid.',
    'unique': 'This {field} already exists.',
}


def make_error_messages(exceptions=None, **constraints) -> dict[str, str]:
    """Makes custom error messages for a form field.

    Args:
        exceptions (list | tuple | None, optional): the exceptions of the constraints (field, min_length, max_length). Defaults to None.
        constraints: the values that will populate the error messages. It can be "field", "min_length" and "max_length".

    Returns:
        dict[str, str]: key and value pairs containing the type of error and its message.
    """
    if not isinstance(exceptions, (list, tuple)) and exceptions is not None:
        raise TypeError('The exceptions must be a list or tuple instance or None.')
    if not exceptions:
        exceptions = []
    errors = {}
    for error_type, error_value in ERROR_MESSAGES.items():
        if error_type in exceptions:
            continue
        errors[error_type] = error_value.format(**constraints)
    return errors


def set_attribute(field, key: str, value: Any) -> None:
    """Takes a key and value pair and sets it in <field>.widget.attrs form field.

    Args:
        field: the form field.
        key (str): the key of the value to be set.
        value (Any): the value to be set.
    """
    if not isinstance(key, str):
        raise TypeError('The key must be a str instance.')
    field.widget.attrs[key] = value


def set_placeholder(field, placeholder: str) -> None:
    """Set the placeholder attribute of a form field.

    Args:
        field: the form field.
        placeholder (str): the placeholder to be set.
    """
    if not isinstance(placeholder, str):
        raise TypeError('The placeholder must be a str instance.')
    set_attribute(field, 'placeholder', placeholder.strip())


def validate_password(password: str) -> None:
    """Checks if the password has at least 1 lowercase letter, 1 uppercase letter, 1 number, 1 special character and 8 characters. If false, raises a ValidationError; otherwise, returns None.

    Args:
        password (str): the password to be validated.

    Raises:
        ValidationError: raised if the password does not meet minimum requirements.
    """
    if not isinstance(password, str):
        raise TypeError('The password must be a str instance.')
    regex = compile(r'^(?=.*[A-Z])(?=.*[\'"!@#$%&*()_\-=+´`\[\]\{\}~^,<.>;:\/?\|])(?=.*[0-9])(?=.*[a-z]).{8,}$')
    if not regex.match(password):
        raise ValidationError('The password must have at least 1 uppercase letter, 1 lowercase letter, 1 number, 1 special character and 8 characters.')
