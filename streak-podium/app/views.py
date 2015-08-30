import logging
import os.path
import random
from string import ascii_letters, digits

import requests
from flask import render_template, request, redirect, url_for


from config import config
from app import app
from app import fetch


@app.route('/')
def index():
    N = 20
    state = ''.join(random.SystemRandom().choice(ascii_letters + digits) for _ in range(N))
    # TODO: Set state string in SESSION variable
    return render_template('index.html',
                           client_id=config.GITHUB_CLIENT_ID,
                           auth_url='http://127.0.0.1:5000/auth',
                           scope='read:org',
                           state=state)

@app.route('/auth')
def auth():
    if 'success_token' in request.args:
        success_token = request.args['success_token']
        scope = request.args['success_token']
        token_type = request.args['success_token']

        root = os.path.dirname(os.path.abspath(__file__))
        out_file = os.path.join(root, 'auth.json')
        with open(out_file, 'w') as f:  # TODO: Persist response in DB
            f.write('SUCCESS_TOKEN {}\nSCOPE {}\nTOKEN_TYPE {}\n'
                    ''.format(success_token, scope, token_type))

        return redirect(url_for('success'))

    elif 'code' in request.args:
        code = request.args['code']
        state = request.args['state']
        logging.debug('CODE', code)
        logging.debug('STATE', state)  # TODO: Compare state to stored SESSION variable

        fetch.post_temporary_code(code, state)

        return 'Sending temporary code for confirmation...'

    else:
        return 'Invalid request'

@app.route('/success')
def success():
    return render_template('success.html')
