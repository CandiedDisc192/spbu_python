from functools import wraps
import warnings
import traceback


def safe_call(function):
    @wraps(function)
    def fake_func(*args, **kwargs):
        try:
            res = function(*args, **kwargs)
        except BaseException as e:
            f_name = function.__name__
            e_type, e_msg = type(e).__name__, str(e)
            e_positions = traceback.format_exc().splitlines()[-3:-1]
            e_full_path, e_code = [line.lstrip() for line in e_positions]
            e_file, e_line = e_full_path.split(",")[:2]
            double_quote = '"'
            warning_info = (
                f'\nError in function {f_name}.\n{e_file.replace(double_quote, "")}\nType: {e_type}\nMessage: {e_msg}\n'
                f"On {e_line.lstrip()}: {e_code}"
            )
            warnings.warn(warning_info)
            return None
        return res

    return fake_func
