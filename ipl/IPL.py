import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget, QHeaderView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from datetime import datetime
from PyQt5.QtCore import Qt


class IPLMatchesGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IPL Match Scores")
        self.setGeometry(100, 100, 2000, 800)  # Increase the window size

        # Create a central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create a table view to display match details
        self.match_table_view = QTableView()
        layout.addWidget(self.match_table_view)

        # Increase the size of the match table view
        self.match_table_view.setMinimumSize(1000, 400)

        # Populate the match table with IPL match details
        self.populate_ipl_matches()

    def populate_ipl_matches(self):
        # Create a model for the match table
        match_model = QStandardItemModel()
        match_model.setHorizontalHeaderLabels(['Away Team', 'Away Score', 'Home Score', 'Home Team', 'Status'])

        # Send a GET request to the cricScore API endpoint for IPL matches
        url = "https://api.cricapi.com/v1/cricScore"
        api_key = "86f604f5-a3ff-4920-a7d2-6869926a57d1"
        params = {"apikey": api_key}
        response = requests.get(url, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response and filter IPL matches
            data = response.json()
            ipl_matches = [match for match in data["data"] if "Indian Premier League" in match.get("series", "")]

            # Sort IPL matches by date and time (ascending order)
            ipl_matches.sort(key=lambda x: datetime.strptime(x["dateTimeGMT"], "%Y-%m-%dT%H:%M:%S"))

            # Add IPL match details to the model
            for match in ipl_matches:
                away_team = match['t1']
                home_team = match['t2']
                status = match['status']
                t1s = match['t1s']
                t2s = match['t2s']

                # Add match details to the match model
                match_row = [QStandardItem(away_team),
                             QStandardItem(str(t1s) if t1s is not None else ""),
                             QStandardItem(str(t2s) if t2s is not None else ""),
                             QStandardItem(home_team),
                             QStandardItem(status)]
                match_model.appendRow(match_row)

                # Highlight the winning team in green and the losing team in red
                if t1s is not None and t2s is not None:
                    if t1s > t2s:
                        for item in match_row[:2]:
                            item.setBackground(Qt.green)
                        for item in match_row[2:4]:
                            item.setBackground(Qt.red)
                    elif t1s < t2s:
                        for item in match_row[:2]:
                            item.setBackground(Qt.red)
                        for item in match_row[2:4]:
                            item.setBackground(Qt.green)

        else:
            print("Error:", response.status_code)

        # Set the model for the match table view
        self.match_table_view.setModel(match_model)

        # Resize the columns to fit the content
        self.match_table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


def main():
    app = QApplication(sys.argv)
    window = IPLMatchesGUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
