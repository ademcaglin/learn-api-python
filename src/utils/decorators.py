from flask import request, abort
from flask import current_app as app
from functools import wraps


def login_not_required(func):
    func._exclude_from_require_login = True
    return func


def require_login():
    login = True
    if request.endpoint in app.view_functions:
        view_func = app.view_functions[request.endpoint]
        login = not hasattr(view_func, '_exclude_from_require_login')
    if login:
        token = request.headers.get("authorization")
        if not token:
            return abort(401)
        user = request.headers.get("authorization")
from flask import request, abort
from functools import wraps

def sample_decorator(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        return f(*args, **kwargs)
   
    return wrap
