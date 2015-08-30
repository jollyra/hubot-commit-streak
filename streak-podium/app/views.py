import random
from string import ascii_letters, digits

from config import config
from app import app

from flask import render_template


@app.route('/')
def index():
    N = 20
    rand_str = ''.join(random.SystemRandom().choice(ascii_letters + digits) for _ in range(N))
    return render_template('index.html',
                           client_id=config.GITHUB_CLIENT_ID,
                           auth_url='http://127.0.0.1:5000/auth',
                           scope='read:org',
                           state=rand_str)

