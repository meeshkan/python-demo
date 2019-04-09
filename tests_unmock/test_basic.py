"""
Basic example showing a single request with `unmock`
Things to note:
    - Summarized with 2 calls - import and initialization
    - Mocks are stored locally if desired, but data is generated off-site and is semantically correct
    - Mocks can be chosen to be non-deterministic (imitating failure points, bad answers, etc)
    - Only required familiarity with call and points of interest, not necessarily the entire response
    - Trivial usage
"""

import requests
import unmock

unmock.init()

def test_unmock_once():
    res = requests.get("https://www.behance.net/v2/projects?api_key=u_n_m_o_c_k_200")
    # This is not guaranteed if we use 'flaky' mode - our code should know how to handle those cases!
    assert res.status_code == 200
    content = res.json()
    assert content.get('projects')
    # We can't determine the exact number (unless we know what our mock contains), but we care about the TYPE
    assert isinstance(content.get('projects')[0].get('id'), int)
    # This should be expected, but we didn't need to code it
    assert "json" in res.headers.get("Content-Type", "")


def test_unmock_missing():
    res = requests.get("http://www.i-forgot-to-set-my-env-variable.com/")
    content = res.json()
    assert content.get('badNews')

def test_unmock_off():
    unmock.reset()
    res = requests.get("http://www.i-forgot-to-set-my-env-variable.com/")
    assert res.status_code == 200  # Got valid response from target URL after shutting down unmock.
