from src.tests.test2.task2 import logger
import datetime
import tempfile
import pytest

FAKE_TIME = datetime.datetime(2022, 12, 12, 12, 30, 30, 777777)


@pytest.fixture
def patch_datetime(monkeypatch):
    class fake_time(datetime.datetime):
        @classmethod
        def now(cls):
            return FAKE_TIME

    monkeypatch.setattr(datetime, "datetime", fake_time)


@pytest.mark.parametrize(
    "arguments,expected",
    (
        ((("100", "33"),), ["12/12/2022 12:30:30 multiply a=100 b=33 3300\n"]),
        ((("www", "ccc"),), ["12/12/2022 12:30:30 multiply a=www b=ccc None\n"]),
        (
            (("100", "33"), ("5", "5"), ("num", "0")),
            [
                "12/12/2022 12:30:30 multiply a=100 b=33 3300\n",
                "12/12/2022 12:30:30 multiply a=5 b=5 25\n",
                "12/12/2022 12:30:30 multiply a=num b=0 None\n",
            ],
        ),
    ),
)
def test_logger(arguments, expected, patch_datetime):
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as templ_file:
        log_file = templ_file.name

        @logger(log_file)
        def multiply(a, b):
            if a.isdigit() and b.isdigit():
                return int(a) * int(b)

        for arg1, arg2 in arguments:
            multiply(arg1, arg2)

        with open(log_file, "r") as file:
            for i in range(len(expected)):
                assert file.readline() == expected[i]
