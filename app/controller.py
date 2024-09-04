# app/controller.py

from flask import Flask, request, jsonify
from app.service import AuthService

app = Flask(__name__)
auth_service = AuthService(db_path="app/users.db")


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    success, message = auth_service.login(username, password)
    return jsonify({"success": success, "message": message}), 200 if success else 401
