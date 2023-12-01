import datetime
from functools import wraps
from inspect import signature


def logger(logs_path):
    def decorator(function):
        @wraps(function)
        def fake_func(*args, **kwargs):
            f_name = function.__name__

            raw_arguments = signature(function).bind(*args, **kwargs)
            arguments = ""
            for key in raw_arguments.arguments:
                if key != "kwargs":
                    arguments += f"{key}={raw_arguments.arguments[key]} "
            if "kwargs" in raw_arguments.arguments:
                for key in raw_arguments.arguments["kwargs"]:
                    arguments += f"{key}={raw_arguments.arguments['kwargs'][key]} "

            time = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
            res = function(*args, **kwargs)
            with open(logs_path, "a") as logs_file:
                logs_file.write(f"{time} {f_name} {arguments.rstrip()} {res}\n")
            return res

        return fake_func

    return decorator
