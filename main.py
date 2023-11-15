# For handling all CRUD operations

from flask import Blueprint, render_template

# All the functions inside main.py will be accessed via the blueprint name "main", eg. main.function_name
main = Blueprint("main", __name__)

# Route to Home Page of the website
@main.route('/')
def home_page():
    return "Hello World"

# Route to the User's Profile page
@main.route('/profile')
def profile():
    return "This is profile page"