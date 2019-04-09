"""
Basic example showing `unmock` integration with `pytest`
Things to note:
    - Supports a command line plugin for unmock (pytest ... --unmock)
        - Flag runs with default options - so you can't change the way it works mid-call (right now)
    - Unmock is not even imported!
"""

import requests
import pytest

def test_flag(pytestconfig):  # The fixture is also just for demonstration!
    has_unmock_flag = pytestconfig.getoption("USE_UNMOCK")  # You don't need to do this; this is for the demo purposes
    res = requests.get("https://www.example.com/")  # Call goes through
    if has_unmock_flag:  # Caught with --unmock
        assert res.json()
    else:
        with pytest.raises(Exception):  # Not caught
            assert res.json()
