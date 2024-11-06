import mysql.connector
from mysql.connector import Error

class UserDAL:
    def __init__(self, host='localhost', user='root', password='sql321', database='python-test'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            # Establish connection to MySQL database
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.conn.is_connected():
                print("Connected to MySQL database")
                self.cursor = self.conn.cursor(dictionary=True)
                self.create_table()
        except Error as e:
            print(f"Database connection failed: {e}")
            self.conn = None

    def create_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            username VARCHAR(255) PRIMARY KEY,
            password VARCHAR(255)
        )
        """
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def get_user(self, username):
        if not self.conn:
            return None
        self.cursor.execute("SELECT username, password FROM users WHERE username = %s", (username,))
        row = self.cursor.fetchone()
        if row:
            return {'username': row['username'], 'password': row['password']}
        return None

    def get_all_users(self):
        if not self.conn:
            return None
        self.cursor.execute("SELECT username FROM users")
        rows = self.cursor.fetchall()
        return [{'username': row['username']} for row in rows] if rows else None

    def add_user(self, username, password):
        if not self.conn:
            return None
        try:
            self.cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            self.conn.commit()
            print(f"User {username} added successfully.")
        except Error as e:
            print(f"Failed to add user: {e}")
