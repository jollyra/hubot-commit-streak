import os.path
import random
from string import ascii_letters, digits

from config import config
from app import app

from flask import render_template, request, redirect, url_for


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
    code = request.args['code']
    state = request.args['state']
    print('CODE', code)
    print('STATE', state)  # TODO: Compare state string to stored SESSION variable

    root = os.path.dirname(os.path.abspath(__file__))
    out_file = os.path.join(root, 'auth.json')
    with open(out_file, 'w') as f:  # TODO: Persist response in DB
        f.write('CODE {}\nSTATE {}\n'.format(code, state))

    return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')
