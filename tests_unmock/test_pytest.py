"""
Basic example showing `unmock` integration with `pytest`
Things to note:
    - Currently uses fixtures, but can easily be extended to use decorators
    - Supports a command line plugin for unmock (pytest ... --unmock) - see `test_pytest_flag`
    - Unmock is not even imported!
"""
import pytest
import requests

def test_simple_fixture(unmock_local):  # Only used locally in this function
    res = requests.get("https://www.example.com/")
    assert res.status_code == 200
    assert res.json()  # unmock is running, response is in JSON file format


def test_modify_options(unmock_local):
    unmock_local(whitelist="www.example.com")  # Reconfigured in-test to control whitelist
    res = requests.get("https://www.example.com/")  # Call goes through
    assert res.status_code == 200
    with pytest.raises(Exception):
        assert res.json()  # Raises as true response from example.com is text and not json

    res = requests.get("https://www.behance.net/v2/projects")  # Still mocked
    assert res.status_code == 200
    assert 'projects' in res.json()
