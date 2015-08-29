from config import config

print(config)

# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash

def init_db():
    from contextlib import closing
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

if __name__ == '__main__':
    # create our little application :)
    app = Flask(__name__)
    app.config.from_object(config)

    print(config.DATABASE)
    #    init_db()
    app.run()

