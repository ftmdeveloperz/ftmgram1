from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# Initialize PyMongo
mongo = PyMongo()

class User(UserMixin):
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def save_to_db(self):
        user_collection = mongo.db.users
        user_collection.insert_one({
            'username': self.username,
            'email': self.email,
            'password': generate_password_hash(self.password)
        })

    @staticmethod
    def find_by_email(email):
        user_collection = mongo.db.users
        user = user_collection.find_one({'email': email})
        if user:
            return User(
                username=user['username'],
                email=user['email'],
                password=user['password']
            )
        return None

    @staticmethod
    def check_password(stored_password, provided_password):
        return check_password_hash(stored_password, provided_password)


class Post:
    def __init__(self, title, description, image_url, author_email):
        self.title = title
        self.description = description
        self.image_url = image_url
        self.author_email = author_email

    def save_to_db(self):
        post_collection = mongo.db.posts
        post_collection.insert_one({
            'title': self.title,
            'description': self.description,
            'image_url': self.image_url,
            'author_email': self.author_email
        })

    @staticmethod
    def find_all_posts():
        post_collection = mongo.db.posts
        return list(post_collection.find())