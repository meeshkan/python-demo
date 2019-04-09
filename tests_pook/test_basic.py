"""
Basic example showing a single request with `pook`
Things to note:
    - Have to use a `utils` module to declutter the unittest, as we have to write the mock manually
    - Have to be familiar with the target API enough to write our own semantically correct mock
    - Have to be familiar with the reply status and specify logical headers
    - All fetched information is known and deterministic
    - At time of testing: pook.off() was broken (hence final test)
"""

import pytest
import pook
import pook.exceptions
import requests
from .utils import BEHANCE_PROJECTS_REPONSE, BHENACE_PROJECTS_LENGTH

pook.on()

# Query parameters have to be explictly written down; you can filter by Headers if needed, though.
pook.get("https://www.behance.net/v2/projects?api_key=u_n_m_o_c_k_200").reply(200).headers(
    {  # Headers also needed to be manually contstructed
        "Content-Length": str(BHENACE_PROJECTS_LENGTH),
        "Content-Type": "application/json; charset=utf-8",
        "ETag": "W/\"5e5e-Skxf9ruz9l1grCAr8kIDbgRdcw8\"",
        "Access-Control-Allow-Origin": "*",
        "X-DNS-Prefetch-Control": "off",
        "X-Frame-Options": "SAMEORIGIN",
        "Strict-Transport-Security": "max-age=15552000; includeSubDomains",
        "X-Download-Options": "noopen",
        "X-Content-Type-Options": "nosniff",
        "X-XSS-Protection": "1; mode=block",
    }
).json(BEHANCE_PROJECTS_REPONSE)

def test_pook_once():
    res = requests.get("https://www.behance.net/v2/projects?api_key=u_n_m_o_c_k_200")
    assert res.status_code == 200  # Hard coded to succeed!
    content = res.json()
    assert content.get('projects')
    assert content.get('projects')[0].get('id') == 1337
    assert "json" in res.headers.get("Content-Type", "")

# Pook raises an exception if no match was found
def test_pook_missing():
    with pytest.raises(pook.exceptions.PookNoMatches):
        res = requests.get("https://www.example.com")

def test_pook_off():
    pook.off()  # Called off.
    with pytest.raises(pook.exceptions.PookNoMatches):  # Still raises even though called off!
        res = requests.get("http://www.i-forgot-to-set-my-env-variable.com/")
