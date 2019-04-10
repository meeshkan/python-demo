import pytest
import json
from .flask_demo import app

TEST_MODE = "pook"  # Set to "unmock" for unmock, "pook" for pook, or None for neither (will make real calls!)

if TEST_MODE is None:
    @pytest.fixture
    def client():  # Recommended way to test Flask (see http://flask.pocoo.org/docs/1.0/testing/)
        yield app.test_client()

elif TEST_MODE == "unmock":
    @pytest.fixture
    def client(unmock_local):  # We only added the unmock fixture! No imports, minimal intrusion to the code.
        # If additional options are needed, one can restart unmock by calling `unmock_local(...)`
        yield app.test_client()

elif TEST_MODE == "pook":
    @pytest.fixture
    def client():
        import pook  # Alternatively, one could use pook decorators, etc.
        pook.on()
        (pook.get("https://www.behance.net/v2/projects?api_key=u_n_m_o_c_k_200")
         .persist()
         .reply(200)
         .json({"projects": "lazy"}))
        yield app.test_client()
        pook.off()

else:
    raise Exception("Unknown test mode {}".format(TEST_MODE))

def test_call(client):
    res = client.get("/")
    content = json.loads(res.data)
    assert "projects" in content
