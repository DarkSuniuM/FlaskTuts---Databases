# Databases!!
import sqlite3
from flask import Flask, g, request


app = Flask(__name__)


def create_db():
    return sqlite3.connect('./db.sqlite')


@app.before_request
def before_request_hook():
    g.db = create_db()
    g.cur = g.db.cursor()


@app.after_request
def after_request_hook(response):
    g.db.close()
    return response


@app.route('/')
def index():
    action = request.args.get('action')
    username = request.args.get('username')
    password = request.args.get('password')
    if action and username and password:
        if action.lower() == 'register':
            try:
                g.cur.execute(
                    'INSERT INTO users (username, password) VALUES (?, ?)',
                    (username, password))
                g.db.commit()
            except sqlite3.IntegrityError:
                g.db.rollback()
                return "User duplicated."
            return "User added."
        if action.lower() == 'login':
            g.cur.execute(
                'SELECT * FROM users WHERE username = ? AND password = ?', 
                (username, password))
            user = g.cur.fetchone()
            if not user:
                return "Invalid Credentials."
            return f"Welcome dear, {user[1]}"
    return "Hello World"
