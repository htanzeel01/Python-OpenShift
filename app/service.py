# app/service.py
import sqlite3

from app.dal import UserDAL
from flask import g
from app.user import User


class AuthService:
    def __init__(self, db_path=":memory:"):
        self.dal = UserDAL(db_path)
        self.dal.connect()
        self.hardcoded_users = [
            User("admin", "admin123"),
            User("user", "user123")
        ]

    def login(self, username, password):
        user_data = self.dal.get_user(username)
        if user_data:
            user = User(user_data['username'], user_data['password'])
            if user.check_password(password):
                return True, "Login successful!"
            return False, "Invalid password."

        # Fallback to hardcoded users
        for user in self.hardcoded_users:
            if user.username == username and user.check_password(password):
                return True, "Login successful! (fallback mode)"

        return False, "User not found."



    def get_db(self):
        if 'db' not in g:
            g.db = sqlite3.connect("app/users.db", check_same_thread=False)
            g.db.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password TEXT
                )
            """)
            g.db.commit()
        return g.db




