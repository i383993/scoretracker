import requests
import subprocess
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem

# Create a new QApplication
app = QApplication([])

# Create a QTableView
view = QTableView()

# Resize the QTableView
view.resize(500, 500)

# Create a QStandardItemModel
model = QStandardItemModel()

# Set the headers for the QStandardItemModel
model.setHorizontalHeaderLabels(['Team 1', 'Score 1', 'Score 2', 'Team 2'])


# Define the teams
team1 = 'Liverpool'
team2 = 'Manchester City'

# Send a GET request to the football-data.org matches endpoint
response = requests.get(f'https://api.football-data.org/v2/matches?team1={team1}&team2={team2}', headers={'X-Auth-Token': '1e83681ff68c4674aaddeb939830faf5'})

# Parse the JSON response
data = response.json()

# Loop through the matches and print the scores
for i, match in enumerate(data['matches']):
    item1 = QStandardItem(team1)
    item2 = QStandardItem(str(match['score']['fullTime']['homeTeam']))
    item3 = QStandardItem(str(match['score']['fullTime']['awayTeam']))
    item4 = QStandardItem(team2)
    model.setItem(i, 0, item1)
    model.setItem(i, 1, item2)
    model.setItem(i, 2, item3)
    model.setItem(i, 3, item4)

# Set the model for the QTableView
view.setModel(model)

# Resize the columns to fit the content
view.resizeColumnsToContents()

# Show the QTableView
view.show()

# Start the Qt event loop
app.exec_()