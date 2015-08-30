import json
import logging

import requests
from flask import url_for

from config import config


def post_temporary_code(code, state):
    url = 'https://github.com/login/oauth/access_token'
    payload = {
        'client_id': config.GITHUB_CLIENT_ID,
        'client_secret': config.GITHUB_CLIENT_SECRET,
        'code': code,
        'redirect_uri': url_for('auth'),
        'state': state,
    }
    r = requests.post(url, data=json.dumps(payload))
    if not r.status_code == requests.codes.ok:
        logging.info('Full authorization succeeded')

