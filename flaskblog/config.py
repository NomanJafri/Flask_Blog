import os

class Config:
    SECRET_KEY = 'bb955930a281a6e6e12a82c41f31770d'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('Email')
    MAIL_PASSWORD = os.environ.get('pass')