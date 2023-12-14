# views.py
from flask import render_template, request, redirect, url_for, session, Blueprint, flash, jsonify
from models import User
from extensions import db, bcrypt
from flask_bcrypt import Bcrypt

views = Blueprint("views", __name__)
bcrypt = Bcrypt()


@views.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = bcrypt.generate_password_hash(request.form["password"]).decode(
            "utf-8"
        )

        if (
            User.query.filter_by(username=username).first()
            or User.query.filter_by(email=email).first()
        ):
            # User already exists
            flash("Username or email already in use.", "error")
            return redirect(url_for("views.signup")), 400

        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("Account created successfully, please login.", "success")
        return redirect(url_for("views.login")), 201

    return render_template("signup.html", title="Sign Up")


@views.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            session["username"] = user.username
            flash("Logged in successfully.", "success")
            return redirect(url_for("views.home")), 200
        else:
            flash("Invalid email or password.", "error")
            return redirect(url_for("views.home")) , 401

    return render_template("login.html", title="Login")


@views.route("/logout")
def logout():
    session.pop("username", None)
    flash("You have been logged out.", "info")
    return redirect(url_for("views.login")) , 200

@views.route("/")
def home():
    if "username" in session:
        return render_template("home.html", title="Home")
    flash("Please login to view this page.", "info")
    return redirect(url_for("views.login")), 200

@views.route("/delete/<user>", methods=['DELETE'])
def delete(user):
    data = User.query.filter_by(username=user).first()
    if data:
        db.session.delete(data)
        db.session.commit()
        session.pop("username", None)
        print('Your account has been deleted!')
        return jsonify({'success': True})
        #return redirect(url_for('views.login')), 200
    else:
        print("Not working")
        return redirect(url_for('views.signup'))
        

@views.route("/update/<user>", methods=['GET', 'PATCH'])
def update(user):
    if request.method == 'GET':
        return render_template("update.html", title="Update")
    else:
        new_password = request.json.get('new_password')
        data = User.query.filter_by(username=user).first()

        if data:
            # Update the password field with the new password
            password = bcrypt.generate_password_hash(new_password).decode("utf-8")
            data.password = password
            # Commit the changes to the database
            db.session.commit()

            print('Your password has been updated!')
            return redirect(url_for("views.login")), 200
        else:
            print('User not found!', 'error')
            return redirect(url_for("views.home")), 404
