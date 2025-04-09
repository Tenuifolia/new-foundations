import sqlite3

connection = sqlite3.connect("competency_tracking.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone TEXT,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    active BOOLEAN DEFAULT 1,
    date_created DATETIME DEFAULT CURRENT_TIMESTAMP,
    hire_date DATE,
    user_type TEXT CHECK(user_type IN ('user', 'manager')) NOT NULL
);
""")


# Some interesting new message
# Something else here



# I'm going to add something even newer here.