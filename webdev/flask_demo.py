import requests
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    # Do some work
    # Our page depends on information from behance, auth from facebook, etc... make the call as you would in production
    res = requests.get("https://www.behance.net/v2/projects?api_key=u_n_m_o_c_k_200")
    # Work with the response as usual - unmock will provide a semantically correct version while testing!
    return res.content