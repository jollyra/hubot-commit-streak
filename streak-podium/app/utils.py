import json
import os.path


def persist_access_token(json_content):
    """ Save our response content to file or DB or whatever. """

    access_token = json_content['access_token']
    scope = json_content['scope']
    token_type = json_content['token_type']

    print('ACCESS_TOKEN', access_token)
    print('SCOPE', scope)
    print('TOKEN_TYPE', token_type)

    root = os.path.dirname(os.path.abspath(__file__))  # TODO: Move path to config
    out_file = os.path.join(root, 'auth.json')
    with open(out_file, 'w') as f:  # TODO: Persist response in DB
        json.dump(json_content, f)


def retrieve_access_token():
    """ Extract tokens & stuff from file or DB or whatever. """
    root = os.path.dirname(os.path.abspath(__file__))  # TODO: Move path to config
    json_file = os.path.join(root, 'auth.json')
    with open(json_file, 'r') as f:  # TODO: Retrieve response from DB
        return json.load(f)

