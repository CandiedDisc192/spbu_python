from time import ctime
from functools import wraps


def spy(function):
    @wraps(function)
    def fake_function(*args, **kwargs):
        if not hasattr(fake_function, "calls_info"):
            fake_function.calls_info = []
        start_time = ctime()
        result = function(*args, **kwargs)
        fake_function.calls_info.append((start_time, {"args": args, "kwargs": kwargs}))
        return result

    return fake_function


def print_usage_statistic(function):
    if not getattr(function, "calls_info", False):
        raise ValueError("spy decorator was not used when creating the function")

    for call_info in function.calls_info:
        yield call_info

