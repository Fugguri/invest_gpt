import sqlite3
from datetime import date


class Database:
    def __init__(self, db_file) -> None:

        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def cbdt(self):
        with self.connection:
            create = """ CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    full_name TEXT,
                    telegram_id TEXT NOT NULL UNIQUE ON CONFLICT IGNORE,
                    username TEXT
                    );

                    """
            self.cursor.executescript(create)

    def add_user(self, full_name, telegram_id, username):
        with self.connection:
            self.cursor.execute(

                f"INSERT INTO users(full_name, telegram_id, username) VALUES('{full_name}', '{telegram_id}', '{username}')"
            )
    def get_all_users(self):
        with self.connection:
            self.cursor.execute("SELECT * FROM users")
            
        return self.cursor.fetchall()

if __name__ == "__main__":
    a = Database("gpt.db")
    a.cbdt()
