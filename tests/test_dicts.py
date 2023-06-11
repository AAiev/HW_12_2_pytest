from utils import dicts


def test_get_val():
    assert dicts.get_val({"one": "1", "two": "2"}, "one", "test") == "1"
    assert dicts.get_val({"one": "1", "two": "2"}, "three", "test") == "test"
    assert dicts.get_val({"one": "1", "two": "2"}, "three") == "git"