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
    print('RETRIEVING orgs from Github')

    json_content = utils.retrieve_access_token()  # Auth info TODO: Which user?

    url = 'https://api.github.com/user/orgs'
    headers = {
        'Accept': 'application/json',
        'Authorization': 'token {}'.format(json_content['access_token']),
    }
    r = requests.get(url, headers=headers)

    if r.status_code == requests.codes.ok:
        print('Response: {} -- Org request succeeded'.format(r.status_code))
    else:
        print('Response: {} -- Org request failed'.format(r.status_code))
    return r


def get_members_in_org(org_login):
    """ Retrieve user orgs. """
    print('RETRIEVING members in org [{}] from Github'.format(org_login))

    json_content = utils.retrieve_access_token()  # Auth info TODO: Which user?

    url = 'https://api.github.com/orgs/{}/members'.format(org_login)
    headers = {
        'Accept': 'application/json',
        'Authorization': 'token {}'.format(json_content['access_token']),
    }
    r = requests.get(url, headers=headers)

    if r.status_code == requests.codes.ok:
        print('Response: {} -- Org Members request succeeded'.format(r.status_code))
    else:
        print('Response: {} -- Org Members request failed'.format(r.status_code))
    return r

