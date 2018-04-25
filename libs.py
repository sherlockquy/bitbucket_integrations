from flask import jsonify
from functools import wraps

def json_response():
    def decorator_func(func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            return jsonify(func(*args, **kwargs))

        return func_wrapper
    return decorator_func