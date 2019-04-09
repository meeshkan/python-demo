"""
Basic example showing modifying behaviour of `unmock`
Things to note:
    - `pook` works by intercepting everything, and supply semantically correct results for APIs in Unmock database.
        - In practice, the code simply runs as normal and you don't have to create your own mocks for end cases.
        - Can whitelist certain calls you'd like to allow via *host* matching (as opposed to specific calls in `pook`)
    - Mocks are "persistent" and do not expire; flaky mode can be used to simulate irregularities. Access time remains
        virtually identical to real API access time (simulating response time etc).
    - Results are mocked if possible, returns a valid response alerting of missing mocks otherwise, while certain calls
        can also be whitelisted.
    - Mocks are identifiable insomuch they have a unique hash and metadata, allowing users to collaborate on mocks,
        sharing edge cases, and expending code.
"""
import unmock
import pytest
import requests


def test_context_manager():
    with unmock.patch():
        res = requests.get("https://www.example.com")
        assert res.status_code == 200
    res = requests.get("https://www.example.com")  # Goes to actual request
    with pytest.raises(Exception):
        assert res.json()


def test_unmock_status():
    unmock.init()
    assert unmock.is_mocking()
    unmock.reset()
    assert not unmock.is_mocking()


def test_unmock_whitelist():
    unmock.init(whitelist="www.example.com")
    res = requests.get("https://www.example.com")  # Unmatched, so it is redirected
    with pytest.raises(Exception):
        assert res.json()
    unmock.reset()


def test_unmock_signature():
    # Because we used different signatures, the content might be identical but the mocks are unique and have their own
    # ID, making sharing them quite easy!
    opts = unmock.init(signature="Hello ", save=True)
    res = requests.get("https://www.example.com")
    opts.signature = "world!"
    res2 = requests.get("https://www.example.com")
    assert res.json() == res2.json()

