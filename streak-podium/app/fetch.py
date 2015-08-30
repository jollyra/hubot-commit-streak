import json
import logging

import requests
from flask import url_for

from config import config


def post_temporary_code(code, state):
    """ POST code & state to Github to get an access token. """

    print('POSTING code and state to Github')

    url = 'https://github.com/login/oauth/access_token'
    payload = {
        'client_id': config.GITHUB_CLIENT_ID,
        'client_secret': config.GITHUB_CLIENT_SECRET,
        'code': code,
        'redirect_uri': url_for('auth', _external=True),
        'state': state,
    }
    r = requests.post(url, data=payload)
    print(r.status_code)
    print(r.content)
    if r.status_code == requests.codes.ok:
        print('Response: {} -- Full authorization succeeded'.format(r.status_code))
        return True
    else:
        print('Response: {} -- Full authorization failed'.format(r.status_code))
        return False

