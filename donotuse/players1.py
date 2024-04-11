from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    # Connect to the SQLite database
    conn = sqlite3.connect('nba.db')

    # Create a cursor
    c = conn.cursor()

    # Retrieve the data
    c.execute("SELECT * FROM players")
    rows = c.fetchall()

    # Close the connection
    conn.close()

    # Render the home.html template and pass the rows to it
    return render_template('home.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)