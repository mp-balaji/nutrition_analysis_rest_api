from flask import Flask
import os
from extensions import db, bcrypt, migrate
from config import DevConfig, ProdConfig

app = Flask(__name__)

env = os.getenv('FLASK_ENV', 'dev')

if env == 'prod':
    app.config.from_object(ProdConfig)
else:
    app.config.from_object(DevConfig)

db.init_app(app)
bcrypt.init_app(app)
migrate.init_app(app, db)

from views import views

app.register_blueprint(views)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)

