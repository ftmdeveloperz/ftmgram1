import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')  # Your Gmail address
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')  # Your Gmail app password
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MONGO_URI = os.environ.get('MONGO_URI')  # Your MongoDB URI
