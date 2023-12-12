import os

class DevConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
    SECRET_KEY = "3bb5854d-c747-420f-823f-98aba5ef5571"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig:
    DEBUG = False

    DB_USERNAME = os.environ.get('DB_USERNAME')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_NAME = os.environ.get('DB_NAME')
    DB_PORT = os.environ.get('DB_PORT', '3306')

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@localhost:{DB_PORT}/{DB_NAME}"
    SECRET_KEY = "3bb5854d-c747-420f-823f-98aba5ef5571"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
