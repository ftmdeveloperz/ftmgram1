from flask import Flask, render_template, redirect, url_for, request, flash
from flask_mail import Mail, Message
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import random
import string

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your secret key

# Initialize Flask extensions
mail = Mail(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Dummy user loader for demonstration
@login_manager.user_loader
def load_user(user_id):
    return UserMixin()  # Replace with actual user loading logic if needed

# Utility function to send OTP
def send_otp(email, otp):
    msg = Message('Your OTP Code', sender=app.config['MAIL_USERNAME'], recipients=[email])
    msg.body = f"Your OTP code is {otp}"
    mail.send(msg)

@app.route('/')
def home():
    posts = []  # Placeholder for posts
    return render_template('index.html', posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']

        # Generate OTP
        otp_code = ''.join(random.choices(string.digits, k=6))
        send_otp(email, otp_code)
        
        flash('Registration successful! Please verify your email with the OTP sent.', 'success')
        return redirect(url_for('verify_otp'))

    return render_template('register.html')

@app.route('/verify_otp', methods=['GET', 'POST'])
def verify_otp():
    if request.method == 'POST':
        email = request.form['email']
        otp = request.form['otp']
        # Dummy check for OTP
        if otp:  # Implement your verification logic here
            flash('Email verified successfully!', 'success')
            return redirect(url_for('login'))
        else:
            flash('Invalid OTP. Please try again.', 'danger')
    return render_template('verify_otp.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Dummy check for login
        if email and password:  # Replace with actual logic
            user_obj = UserMixin()  # Replace with actual user object
            login_user(user_obj)
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials.', 'danger')
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
        # Handle content as needed (e.g., store in a list)
        flash('Post created successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('post.html')

@app.route('/profile')
@login_required
def profile():
    # Dummy placeholder for user posts
    user_posts = []  # Replace with actual user post fetching logic
    return render_template('profile.html', posts=user_posts)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
