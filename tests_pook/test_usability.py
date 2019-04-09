"""
Basic example showing modifying behaviour of `pook`
Things to note:
    - `pook` works by intercepting everything, but will only supply results for specific endpoints, which you have to
        manually write yourself (method, url, query parameters) - you can be very specific to allow "routing", by
        matching based on body, etc
        - Enabling for specific hostnames seems to be broken too
    - Allows for highly fine-tuned mocking system; you still have to mock it all by hand.
        - Modular and chainable with use of `Fluent` (i.e. pook.get(...).reply(...).json(...) etc)
    - Raises Error for unmatched mocks, or allows sending the request through, no middle ground
    - Mocks are, by default, not persistent and after expiring will raise an exception
    - Mocks are identifiable insomuch they are hand written somewhere in the code.
"""
import pook
import pytest
import requests


def test_context_manager():
    with pook.use():
        pook.get("https://www.example.com", reply=204)
        res = requests.get("https://www.example.com")
        assert res.status_code == 204
    # requests.get("http://server.com")  # Scope manager again seems to not have effect (uncomment)


def test_pook_status():
    pook.on()
    assert pook.isactive()
    pook.off()
    assert not pook.isactive()


@pytest.mark.skipif(True, reason="whitelisting also seems broken")
def test_pook_whitelist():
    pook.on()
    # pook.enable_network("www.example.com")  # Broken, at least on Python 3.7
    pook.enable_network()
    res = requests.get("https://www.example.com")  # Unmatched, so it is redirected
    with pytest.raises(Exception):
        assert res.json()
    pook.off()


def test_persistent():
    pook.on()
    pook.get("https://www.example.com").persist().reply(200).json({"data": True})
    for counter in range(5):
        res = requests.get("https://www.example.com")
        assert res.json().get('data')
    pook.off()


def test_pook_pending():
    pook.on()
    pook.get("https://www.example.com").times(2).reply(200).json({"data": True})
    for counter in [1, 0]:
        res = requests.get("https://www.example.com")
        assert res.json().get('data')
        assert pook.pending() == counter

    with pytest.raises(Exception):  # Will throw as there's no mocks
        res = requests.get("https://www.example.com")

    pook.off()


def test_pook_content_matching():
    pook.on()
    pook.get("https://www.example.com").times(2).body("abc").reply(200).json({"data": True})
    res = requests.get("https://www.example.com", data="abc")
    assert res.json().get('data')
    with pytest.raises(Exception):
        requests.get("https://www.example.com", data="def")  # Will throw once again
    pook.off()
