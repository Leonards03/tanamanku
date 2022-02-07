from functools import wraps

from flask import redirect, url_for
from flask_login import current_user


def check_if_authenticated(func):
    @wraps(func)
    def wrapper_check_auth(*args, **kwargs):
        if current_user.is_authenticated:
            if current_user.role.name == 'Admin':
                return redirect(url_for('admin.dashboard'))
            return redirect(url_for('base.index'))
        return func(*args, **kwargs)
    return wrapper_check_auth
