# FTMGRAM

FTMGRAM is a social media platform inspired by Instagram. It allows users to register, log in, post updates, and interact with other users. This platform is built with Flask, MongoDB, and styled to resemble Instagram.

## Features

- User Registration and Login with OTP verification via email.
- Ability to post updates.
- Follow and unfollow users.
- Like and comment on posts.
- View and manage user profiles.

## Requirements

- Python 3.11.4
- Flask
- Flask-PyMongo
- Flask-Mail
- Flask-Login
- pymongo
- werkzeug

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/yourusername/ftmgram.git
    cd ftmgram
    ```

2. **Create and activate a virtual environment**:

    ```sh
    python -m venv venv
    source venv/bin/activate  # For Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Create a `.env` file** in the root directory with the following content:

    ```plaintext
    FLASK_ENV=development
    FLASK_APP=app.py

    # MongoDB configuration
    MONGO_URI=mongodb://localhost:27017/ftmgram

    # Flask-Mail configuration
    MAIL_SERVER=smtp.gmail.com
    MAIL_PORT=587
    MAIL_USERNAME=funtoonsmultimedia@gmail.com
    MAIL_PASSWORD=YOUR_EMAIL_PASSWORD
    MAIL_USE_TLS=True
    MAIL_USE_SSL=False

    # Flask-Login configuration
    SECRET_KEY=your_secret_key_here
    ```

5. **Run the application**:

    ```sh
    flask run
    ```

## Deployment

To deploy this application on a platform like Heroku:

1. **Commit your code to Git**:

    ```sh
    git add .
    git commit -m "Initial commit"
    ```

2. **Create a `Procfile`** with the following content:

    ```plaintext
    web: python app.py
    ```

3. **Create a `runtime.txt`** with the Python version:

    ```plaintext
    python-3.11.4
    ```

4. **Push your code to Heroku**:

    ```sh
    heroku create
    git push heroku main
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to open issues or submit pull requests to improve the platform.

## Contact

For any questions or support, contact [funtoonsmultimedia@gmail.com](mailto:funtoonsmultimedia@gmail.com).