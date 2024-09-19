
import os
import secrets

class Config:
    # Generate a secure random SECRET_KEY if not provided via environment variable
    SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_hex(24)
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')  # Your Gmail address
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')  # Your Gmail app password
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MONGO_URI = os.environ.get('MONGO_URI')  # Your MongoDB URI
