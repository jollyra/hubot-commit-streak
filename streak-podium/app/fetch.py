import json
import logging

import requests
from flask import url_for

from app import utils
from config import config


def post_temporary_code(code, state):
    """ POST code & state to Github to get an access token. """

    print('POSTING code and state to Github')

    url = 'https://github.com/login/oauth/access_token'
    header = {'Accept': 'application/json'}
    payload = {
        'client_id': config.GITHUB_CLIENT_ID,
        'client_secret': config.GITHUB_CLIENT_SECRET,
        'code': code,
        'redirect_uri': url_for('auth', _external=True),
        'state': state,
    }
    r = requests.post(url, headers=header, data=payload)

    if r.status_code == requests.codes.ok:
        print('Response: {} -- Full authorization succeeded'.format(r.status_code))
    else:
        print('Response: {} -- Full authorization failed'.format(r.status_code))
    return r


def get_orgs_for_user():
    """ Retrieve user orgs. """
    # TODO: Which user??
    print('RETRIEVING orgs from Github')

    json_content = utils.retrieve_access_token()  # Auth info

    url = 'https://github.com//user/orgs'
    headers = {
        'Accept': 'application/json',
        'Authorization': 'token {}'.format(json_content['access_token']),
    }
    # payload = {
    #     'client_id': config.GITHUB_CLIENT_ID,
    #     'client_secret': config.GITHUB_CLIENT_SECRET,
    #     'code': code,
    #     'redirect_uri': url_for('auth', _external=True),
    #     'state': state,
    # }
    # r = requests.post(url, headers=header, data=payload)
    r = requests.post(url, headers=headers)

    if r.status_code == requests.codes.ok:
        print('Response: {} -- Org request succeeded'.format(r.status_code))
    else:
        print('Response: {} -- Org request failed'.format(r.status_code))
    return r


