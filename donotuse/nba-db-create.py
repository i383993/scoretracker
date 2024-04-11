import sqlite3

# Connect to the SQLite database. This will create the database if it doesn't exist.
conn = sqlite3.connect('nba.db')

# Create a cursor
c = conn.cursor()

# Create a table
c.execute('''
    CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY,
        full_name TEXT,
        team_id INTEGER,
        is_active INTEGER,
        pts INTEGER
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()