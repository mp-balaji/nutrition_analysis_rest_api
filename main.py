# For handling all CRUD operations
import requests
import numpy as np
import json
from json import JSONEncoder
from flask import Blueprint, render_template, redirect, url_for, request, flash, abort, jsonify

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
# from this get request we are take meal details from the user and sending those details via form post action 
@main.route('/create_meal')
def new_meal():
    return render_template('create_meal.html')

# from this post request we are fetching meal details taken from the user and calling then the api
@main.route('/create_meal', methods=['POST'])
def new_meal_post():

    meals = request.form.get('meals')
    # removing spaces then converting into list using seperator as line break
    meals = meals.strip().split("\r\n")
    print(meals)
    
    endpoint = 'https://api.edamam.com/api/nutrition-details'
    params = {
        'app_id': "72acb605",
        'app_key': "cef3a8d1b3c9911ad144644700d236ee",
    }   
    input = {
        'ingr': meals,
    }
    
    response = requests.post(endpoint, params=params, json=input)
    
    if response.status_code == 200:
        # dt_str = dt.strftime("%Y-%m-%d %H:%M:%S") 
        data = response.json()
        # calories = data.get('calories', {})
        nutrients = data.get('totalNutrients', {})

        res = {
            "Meals":meals,
            "Energy" : str(np.round(nutrients["ENERC_KCAL"]["quantity"],2)) + str(nutrients["ENERC_KCAL"]["unit"]),
            "Protiens": str(np.round(nutrients["PROCNT"]["quantity"],2))+ str(nutrients["PROCNT"]["unit"])
            }
        # instead of redirecting we will render same page from we have taken input will output below
        return redirect(url_for('profile'))
        
    else:
        # print(f"Error: {response.status_code}")
        return(render_template("failure.html", error_message = response.status_code))
    
