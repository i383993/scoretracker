import sys
import requests
import pandas as pd
import sqlite3
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt

# Create a new QApplication
app = QApplication([])

# Create a QTableView
view = QTableView()

# Resize the QTableView
view.resize(500, 500)

# Create a QStandardItemModel
model = QStandardItemModel()

# Set the headers for the QStandardItemModel
model.setHorizontalHeaderLabels(['Home Team', 'Score', 'Away Team'])

# Send a GET request to the football-data.org matches endpoint for the Premier League
response = requests.get('https://api.football-data.org/v4/competitions/PL/matches', headers={'X-Auth-Token': 'debf4e80fd9e4b9f9eec8d80de414a20'})

# Initialize an empty DataFrame with the desired column names
df = pd.DataFrame(columns=['home_team', 'home_score', 'away_team', 'away_score'])

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Loop through the matches and add them to the model
    for match in data.get('matches', []):
        home_team = match.get('homeTeam', {}).get('name', 'Unknown')
        away_team = match.get('awayTeam', {}).get('name', 'Unknown')
        home_score = match['score']['fullTime']['home'] if 'home' in match['score']['fullTime'] else None
        away_score = match['score']['fullTime']['away'] if 'away' in match['score']['fullTime'] else None

        # Create a new DataFrame row and append it to the existing DataFrame
        new_row = pd.DataFrame([[home_team, home_score, away_team, away_score]], columns=df.columns)
        df = pd.concat([df, new_row], ignore_index=True)

# Create a connection to the SQLite database
conn = sqlite3.connect('games.db')

# Write the DataFrame to the SQLite database
df.to_sql('football', conn, if_exists='replace', index=False)

# Close the connection to the SQLite database
conn.close()