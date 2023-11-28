import pytest
from src.homeworks.homework5.task2 import *
from io import StringIO


@pytest.mark.parametrize(
    "string,expected",
    [
        ("aaaabbсaa", "a4b2с1a2"),
        ("a", "a1"),
        (
            "ccaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbba",
            "c2a46b13a1",
        ),
        (
            "abcaabbccaaabbbcccaaaabbbbccccaaaaabbbbbccccc",
            "a1b1c1a2b2c2a3b3c3a4b4c4a5b5c5",
        ),
    ],
)
def test_encode_string(string, expected):
    assert encode_string(string) == expected


def test_encode_string_value_error():
    with pytest.raises(ValueError):
        encode_string("")
    with pytest.raises(ValueError):
        encode_string("a1b2c3")
    with pytest.raises(ValueError):
        encode_string("aaa bbb ccc ddd")


@pytest.mark.parametrize(
    "string,expected",
    [
        ("a4b2с1a2", "aaaabbсaa"),
        ("a1", "a"),
        (
            "c2a46b13a1",
            "ccaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbba",
        ),
        (
            "a1b1c1a2b2c2a3b3c3a4b4c4a5b5c5",
            "abcaabbccaaabbbcccaaaabbbbccccaaaaabbbbbccccc",
        ),
    ],
)
def test_decode_string(string, expected):
    assert decode_string(string) == expected


def test_decode_string_value_error():
    with pytest.raises(ValueError):
        decode_string("")
    with pytest.raises(ValueError):
        decode_string("a")
    with pytest.raises(ValueError):
        decode_string(" a10 b20")
    with pytest.raises(ValueError):
        decode_string("aa10b2")


@pytest.mark.parametrize(
    "fun,user_string,expected",
    [
        (encode_string, "aabbcc", "a2b2c2"),
        (decode_string, "a3b10c1", "aaabbbbbbbbbbc"),
        (encode_string, "", "Given string is empty"),
        (decode_string, " a10 b2/", "Given string contains unnecessary symbols"),
    ],
)
def test_represent_function(fun, user_string, expected):
    assert represent_function(fun, user_string) == expected


@pytest.mark.parametrize(
    "user_input,expected",
    [
        (iter(["3"]), "Undefined option.\n"),
        (iter(["1", "aabb"]), "a2b2\n"),
        (
            iter(["1.", "a1b2c3"]),
            "Given string contains numbers or other unnecessary symbols\n",
        ),
        (
            iter(["1", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaacc"]),
            "a58c2\n",
        ),
        (iter(["1", f'b{"a"*1000}b{"c"*2123}']), "b1a1000b1c2123\n"),
        (iter(["1", ""]), "Given string is empty\n"),
        (iter(["2.", "a100b100c10000"]), f'{"a" * 100}{"b" * 100}{"c" * 10000}\n'),
        (
            iter(["2", "aa1b2c3"]),
            "Incorrect encoding format: letters amount dont match numbers amount\n",
        ),
        (iter(["2", " a2 b3 c4"]), "Given string contains unnecessary symbols\n"),
        (iter(["2", ""]), "Given string is empty\n"),
        (iter(["2", "a2b3c4a2c1"]), "aabbbccccaac\n"),
    ],
)
def test_main(monkeypatch, user_input, expected):
    monkeypatch.setattr("builtins.input", lambda _: next(user_input))
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    assert fake_output.getvalue() == expected
