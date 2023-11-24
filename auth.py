# Handles the authentication part

from flask import Blueprint, render_template, redirect, url_for, request, flash, abort

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():

    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return render_template('home_page.html')