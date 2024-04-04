import pandas as pd
import requests
import json
import sqlite3
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QColor

BASE_URL = "http://api.balldontlie.io"
ALL_JSON = "/v1/games"
# Create a connection to the SQLite database
# It doesn't matter if the database doesn't yet exist
conn = sqlite3.connect('games.db')
# Create a cursor object
c = conn.cursor()

# Create a new table
c.execute('''
    CREATE TABLE IF NOT EXISTS games (
        home_team TEXT,
        home_score INTEGER,
        visitor_team TEXT,
        visitor_score INTEGER
    )
''')

# Define the query parameters
params = {
    'dates[]': ['2024-02-20', '2024-02-21', '2024-02-22','2024-02-23']
}

# Define headers
headers = {
    'Authorization': 'dcbe01ca-2080-4356-b44a-b52f95aae369'
}

# Send the GET request with the query parameters and headers
response = requests.get(BASE_URL + ALL_JSON, params=params, headers=headers)

# Check if the response is valid
if response.status_code == 200:
    data = json.loads(response.text)

    # Create a DataFrame to store the team names and scores
    df = pd.DataFrame(columns=["Home Team", "Home Score", "Visitor Team", "Visitor Score"])

    # Loop through the data and extract the team names and scores
    for game in data['data']:
        home_team = game['home_team']['full_name']
        visitor_team = game['visitor_team']['full_name']
        home_score = game['home_team_score']
        visitor_score = game['visitor_team_score']
        c.execute('''
        INSERT INTO games (home_team, home_score, visitor_team, visitor_score)
        VALUES (?, ?, ?, ?)
    ''', (home_team, home_score, visitor_team, visitor_score))

# Loop through the DataFrame and insert each row into the games table
for i in range(len(df)):
    home_team = df.iat[i, 0]
    home_score = df.iat[i, 1]
    visitor_team = df.iat[i, 2]
    visitor_score = df.iat[i, 3]
    c.execute('''
        INSERT INTO games (home_team, home_score, visitor_team, visitor_score)
        VALUES (?, ?, ?, ?)
    ''', (home_team, home_score, visitor_team, visitor_score))

# Commit the transaction and close the connection
conn.commit()
conn.close()    