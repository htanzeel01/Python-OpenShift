# app/controller.py

from flask import Flask, request, jsonify, render_template, redirect, url_for
from app.service import AuthService

app = Flask(__name__)
auth_service = AuthService(db_path="app/users.db")

@app.route('/')
def home():
    users = auth_service.get_all_users()  # Fetch all users from the service
    print(f"Fetched users: {users}")  # Debugging: print the fetched users
    if users is None:  # Handle the case when users is None
        return jsonify(message="No users found"), 404
    usernames = [user['username'] for user in users]
    return jsonify(usernames=usernames)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.json
        username = data.get('username')
        password = data.get('password')

        success, message = auth_service.login(username, password)
        return jsonify({"success": success, "message": message}), 200 if success else 401
    return render_template('login.html')  # Render the login page for GET requests
