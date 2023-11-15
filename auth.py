# Handles the authentication part

from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def signup():
    return 'This is signup page'


@auth.route('/login')
def login():
    return 'this is login page'


@auth.route('/logout')
def logout():
    return 'this is logout page'