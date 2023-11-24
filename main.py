# For handling all CRUD operations

from flask import Blueprint, render_template, redirect, url_for, request, flash, abort

# All the functions inside main.py will be accessed via the blueprint name "main", eg. main.function_name
main = Blueprint("main", __name__)

# Route to Home Page of the website
@main.route('/')
def home_page():
    return render_template('home_page.html')

# Route to the User's Profile page
@main.route('/profile')
def profile():
    return render_template('profile.html')