import sys
import requests
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

        # Add match details to the model
        row = [QStandardItem(home_team), QStandardItem(f"{home_score if home_score is not None else 'N/A'} - {away_score if away_score is not None else 'N/A'}"), QStandardItem(away_team)]
        model.appendRow(row)

        # Highlight the home team as green if its score is more, and the away team as red
        if home_score is not None and away_score is not None:
            if home_score > away_score:
                for i in range(3):
                    model.item(model.rowCount() - 1, i).setBackground(Qt.green)
            elif home_score < away_score:
                for i in range(3):
                    model.item(model.rowCount() - 1, i).setBackground(Qt.red)

else:
    print(f"Error: {response.status_code}")

# Set the model for the QTableView
view.setModel(model)

# Resize the columns to fit the content
view.resizeColumnsToContents()

# Show the QTableView
view.show()

# Start the Qt event loop
sys.exit(app.exec_())
