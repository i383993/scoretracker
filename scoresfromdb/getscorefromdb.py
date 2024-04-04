from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QColor
import sqlite3


# Create a new QApplication
app = QApplication([])

# Create a QTableView
view = QTableView()

# Resize the QTableView
view.resize(800, 600)

# Create a QStandardItemModel
model = QStandardItemModel()

# Set the headers for the QStandardItemModel
model.setHorizontalHeaderLabels(['Home Team', 'Home Score', 'Visitor Team', 'Visitor Score'])

# Create a connection to the SQLite database
conn = sqlite3.connect('games.db')

# Create a cursor object
c = conn.cursor()

# Execute a SELECT statement to get all rows from the games table
c.execute('SELECT * FROM games')

# Fetch all rows from the cursor
rows = c.fetchall()

# Add the rows to the QStandardItemModel
for i in range(len(rows)):
    for j in range(len(rows[i])):
        item = QStandardItem(str(rows[i][j]))
        if j == 1 and rows[i][j] > rows[i][j+2]:
            item.setForeground(QColor('green'))
        elif j == 3 and rows[i][j] > rows[i][j-2]:
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

# Start the Qt event loop
app.exec_()