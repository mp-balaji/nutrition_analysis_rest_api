from flask import Flask
from extensions import db, bcrypt, migrate

app = Flask(__name__)

DB_IP = "paste_your_ip_address"

# SQLITE Local Settings
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
# app.config["SECRET_KEY"] = "3bb5854d-c747-420f-823f-98aba5ef5571"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# MySQL Compute Engine Settings
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://admin:Adm1n$123@{DB_IP}/nutrition_app"
app.config["SECRET_KEY"] = "3bb5854d-c747-420f-823f-98aba5ef5571"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
bcrypt.init_app(app)
migrate.init_app(app, db)

from views import views

app.register_blueprint(views)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
