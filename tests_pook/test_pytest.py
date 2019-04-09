"""
Basic example showing `pook` integration with `pytest`
Things to note:
    - As `off` doesn't work - there is redundancy in this file, but it's meant to give a sample of the different
        decorators available as pytest integration
"""

import pytest
import pook
import pook.exceptions
import requests


@pook.get('server.com/bar', reply=204)  # Turns pook on for a single call
def test_decorator():
    res = requests.get('http://server.com/bar')
    assert res.status_code == 204


@pook.activate  # Activates pook for this function
def test_simple_pook_request():
    pook.get('server.com/foo').reply(204)  # Capture defined inline
    res = requests.get('http://server.com/foo')
    assert res.status_code == 204


@pook.on  # Identical to above
def test_enable_engine():
    pook.get('server.com/foo').reply(204)
    res = requests.get('http://server.com/foo')
    assert res.status_code == 204
    pook.disable()
    # requests.get("http://server.com/")  # Seems to have no effect at time of writing (uncomment)
