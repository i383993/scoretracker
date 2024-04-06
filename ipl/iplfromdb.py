import sqlite3
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QColor

# Connect to the SQLite database
conn = sqlite3.connect('games.db')
cursor = conn.cursor()

# Execute a SELECT query to retrieve the data
cursor.execute("SELECT * FROM ipl")
data = cursor.fetchall()

# Create a new QApplication
app = QApplication([])

# Create a QTableView
view = QTableView()

# Resize the QTableView
view.resize(500, 500)

# Create a QStandardItemModel
model = QStandardItemModel()

# Set the headers for the QStandardItemModel
model.setHorizontalHeaderLabels(['Home Team', 'Home Score', 'Home Wickets', 'Visitor Team', 'Visitor Score', 'Visitor Wickets'])

# Loop through the data and add each row to the QStandardItemModel
for i, row in enumerate(data):
    for j, value in enumerate(row):
        item = QStandardItem(str(value))
        # Compare home_score to visitor_score and change the background color accordingly

        if j in [0,1, 2] and row[1] > row[4]:  # home_score > visitor_score
            item.setBackground(QColor('green'))
        elif j in [0,1, 2] and row[1] < row[4]:  # home_score < visitor_score
            item.setBackground(QColor('red'))

        elif j in [3,4, 5] and row[4] > row[1]:  # visitor_score > home_score
            item.setBackground(QColor('green'))
        elif j in [3,4, 5] and row[4] < row[1]:  # visitor_score < home_score
            item.setBackground(QColor('red'))
        model.setItem(i, j, item)

# Set the model for the QTableView
view.setModel(model)

# Resize the columns to fit the content
view.resizeColumnsToContents()

# Show the QTableView
view.show()

# Start the Qt event loop
app.exec_()