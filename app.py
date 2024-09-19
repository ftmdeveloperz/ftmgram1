from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_mail import Mail, Message
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_pymongo import PyMongo
import os
from twilio_otp import send_otp
from config import Config
from models import User, Post

app = Flask(__name__)
app.config.from_object(Config)

# Initialize Flask extensions
mongo = PyMongo(app)
mail = Mail(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)

@app.route('/')
def home():
    posts = mongo.db.posts.find().sort('date', -1)
    return render_template('index.html', posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        
        # Generate and send OTP
        otp_code = '123456'  # In a real application, generate a random OTP
        if send_otp(phone, otp_code):
            # Store user data and OTP
            mongo.db.users.insert_one({
                'username': username,
                'email': email,
                'phone': phone,
                'password': password,
                'otp': otp_code,
                'is_verified': False
            })
            flash('Registration successful! Please verify your phone number with the OTP sent.', 'success')
            return redirect(url_for('verify_otp'))
        else:
            flash('Failed to send OTP. Please try again.', 'danger')

    return render_template('register.html')

@app.route('/verify_otp', methods=['GET', 'POST'])
def verify_otp():
    if request.method == 'POST':
        phone = request.form['phone']
        otp = request.form['otp']
        user = mongo.db.users.find_one({'phone': phone, 'otp': otp})
        if user:
            mongo.db.users.update_one({'phone': phone}, {'$set': {'is_verified': True}})
            flash('Phone number verified successfully!', 'success')
            return redirect(url_for('login'))
        else:
            flash('Invalid OTP. Please try again.', 'danger')
    return render_template('verify_otp.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = mongo.db.users.find_one({'email': email, 'password': password})
        if user and user['is_verified']:
            user_obj = User(user['_id'], user['username'], email, user['phone'])
            login_user(user_obj)
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials or phone number not verified.', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    if request.method == 'POST':
        content = request.form['content']
        mongo.db.posts.insert_one({
            'author': current_user.id,
            'content': content,
            'date': datetime.utcnow()
        })
        flash('Post created successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('post.html')

@app.route('/profile')
@login_required
def profile():
    user_posts = mongo.db.posts.find({'author': current_user.id}).sort('date', -1)
    return render_template('profile.html', posts=user_posts)

if __name__ == '__main__':
    app.run(debug=True, port=5000)