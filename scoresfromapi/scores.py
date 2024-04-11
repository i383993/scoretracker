import pandas as pd
import requests
import json
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QColor

BASE_URL = "http://api.balldontlie.io"
ALL_JSON = "/v1/games"

# Define the query parameters
params = {
    'dates[]': ['2024-04-09']
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

        new_row = pd.DataFrame([[home_team, home_score, visitor_team, visitor_score]], columns=df.columns)
        df = pd.concat([df, new_row], ignore_index=True)
# Create a new QApplication
app = QApplication([])

# Create a QTableView
view = QTableView()

# Resize the QTableView
view.resize(600, 500)

# Create a QStandardItemModel
model = QStandardItemModel()

# Set the headers for the QStandardItemModel
model.setHorizontalHeaderLabels(df.columns)

for i in range(len(df)):
    for j in range(len(df.columns)):
        item = QStandardItem(str(df.iat[i, j]))
        if df.columns[j] in ['Home Team', 'Home Score'] and df.iat[i, 1] > df.iat[i, 3]:
            item.setForeground(QColor('green'))
        elif df.columns[j] in ['Visitor Team', 'Visitor Score'] and df.iat[i, 3] > df.iat[i, 1]:
            item.setForeground(QColor('green'))
        else:
            item.setForeground(QColor('red'))
        model.setItem(i, j, item)

# Set the model for the QTableView
view.setModel(model)

# Resize the columns to fit the content
view.resizeColumnsToContents()

# Show the QTableView
view.show()
# Start the QApplication event loop
app.exec_()