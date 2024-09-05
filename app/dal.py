import sqlite3

class UserDAL:
    def __init__(self, db_path=":memory:"):
        self.db_path = db_path

    def connect(self):
        try:
            # Add check_same_thread=False to allow using this connection across threads
            self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
            self.cursor = self.conn.cursor()
            self.create_table()
        except sqlite3.Error as e:
            print(f"Database connection failed: {e}")
            self.conn = None

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT
            )
        """)
        self.conn.commit()

    def get_user(self, username):
        if not self.conn:
            return None
        self.cursor.execute("SELECT username, password FROM users WHERE username = ?", (username,))
        row = self.cursor.fetchone()
        if row:
            return {'username': row[0], 'password': row[1]}
        return None

    def get_all_users(self):
        if not self.conn:
            return None
        self.cursor.execute("SELECT username FROM users")
        rows = self.cursor.fetchall()
        return [{'username': row[0]} for row in rows] if rows else None



