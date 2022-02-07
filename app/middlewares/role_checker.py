import functools

from flask_login import current_user
from werkzeug.exceptions import Unauthorized, abort


def check_permission(allowed_role):
    def decorator_check_permission(func):
        @functools.wraps
        def wrapper_check_permission(*args, **kwargs):
            current_user_role = current_user.role.name
            if current_user_role != allowed_role:
                abort(Unauthorized)

            return func(*args, **kwargs)
        return wrapper_check_permission
    return decorator_check_permission
