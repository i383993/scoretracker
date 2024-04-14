import sys
import sqlite3
import pandas as pd
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

# Create a connection to the SQLite database
conn = sqlite3.connect('games.db')

# Read the data from the SQLite database into a DataFrame
df = pd.read_sql_query("SELECT * FROM football", conn)

# Close the connection to the SQLite database
conn.close()

# Loop through the DataFrame and add the data to the model
for index, row in df.iterrows():
    home_team = row['home_team']
    away_team = row['away_team']
    home_score = int(row['home_score']) if pd.notnull(row['home_score']) else None
    away_score = int(row['away_score']) if pd.notnull(row['away_score']) else None

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

# Set the model for the QTableView
view.setModel(model)

# Resize the columns to fit the content
view.resizeColumnsToContents()

# Show the QTableView
view.show()

# Start the Qt event loop
sys.exit(app.exec_())