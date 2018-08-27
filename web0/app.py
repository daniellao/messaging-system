from flask import Flask
from requests_oauthlib import OAuth1
import requests
from urllib.parse import urlencode
import simplejson as json
from werkzeug.serving import run_simple

app = Flask(__name__)

store_url = 'http://localhost:8071'
endpoint = '/wc-auth/v1/authorize'
params = {
    "app_name": "web2",
    "scope": "read_write",
    "user_id": 123,
    "return_url": "https://localhost:5000/return-page",
    "callback_url": "https://localhost:5000/callback-endpoint"
}

query_string = urlencode(params)

print("%s%s?%s" % (store_url, endpoint, query_string))

@app.route('/callback-endpoint')
def main():
    return 'hello'

if __name__ == "__main__":
    run_simple('localhost', 5000, app, use_reloader=True, use_debugger=True,
           ssl_context=('/app/key.crt',
                        '/app/key.key'))
