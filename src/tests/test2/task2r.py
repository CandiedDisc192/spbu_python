from functools import wraps
import warnings
import traceback
import sys


def safe_call(function):
    @wraps(function)
    def fake_func(*args, **kwargs):
        try:
            res = function(*args, **kwargs)
        except BaseException as e:
            f_name = function.__name__
            e_type, e_msg = type(e).__name__, str(e)
            data = traceback.extract_tb(sys.exc_info()[2])[-1]
            warning_info = (
                f"\nError in function {f_name}.\nFile {data.filename}\nType: {e_type}\nMessage: {e_msg}\n"
                f"On line {data.lineno}: {data.line}"
            )
            warnings.warn(warning_info)
            return None
        return res

    return fake_func
