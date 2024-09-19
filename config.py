import os

class Config:
    # Flask configuration
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')
    SESSION_COOKIE_SECURE = False  # Set to True if using HTTPS

    # MongoDB configuration
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/ftmgram')

    # Email configuration
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'your-email@gmail.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'your-email-password')
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    # Optional: You can add more configuration settings as needed