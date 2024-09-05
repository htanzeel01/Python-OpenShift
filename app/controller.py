# app/controller.py

from flask import Flask, request, jsonify, render_template, redirect, url_for
from app.service import AuthService

app = Flask(__name__)
auth_service = AuthService(db_path="app/users.db")

@app.route('/')
def home():
    # Fetch all users from the service
    users = auth_service.get_all_users()

    # Extract usernames
    usernames = [user['username'] for user in users]

    # Print usernames (this will be shown in the server logs, not the response)
    for username in usernames:
        print(username)

    # Return the usernames as a JSON response
    return jsonify(usernames)
# @app.route('/')
# def home():
#     users = ['Alice', 'Bob', 'Charlie']
#     return render_template('home.html', users=users)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.json
        username = data.get('username')
        password = data.get('password')

        success, message = auth_service.login(username, password)
        return jsonify({"success": success, "message": message}), 200 if success else 401
    return render_template('login.html')  # Render the login page for GET requests
