import sqlite3
import tkinter as tk
from tkinter import ttk
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.http import NBAStatsHTTP
# Connect to the SQLite database
conn = sqlite3.connect('nba.db')
NBAStatsHTTP.timeout = 100  # in seconds

# Get all players
nba_players = players.get_players()

# Create a cursor
c = conn.cursor()

# Create the players table
c.execute('''
    CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY,
        full_name TEXT,
        team_id INTEGER,
        is_active INTEGER,
        pts INTEGER
    )
''')


# Find a specific player
player = [player for player in nba_players if player['full_name'] == 'Jaylen Brown'][0] 

# Get game log for the player
player_log = playergamelog.PlayerGameLog(player_id=player['id'])
logs = player_log.get_data_frames()[0]
total_score = logs['PTS'].sum()
c.execute("INSERT INTO players (id, full_name, is_active, pts) VALUES (?, ?, ?, ?)", 
              (player['id'], player['full_name'], player['is_active'], 55))

# Commit the changes
conn.commit()

# Create a new Tkinter window
window = tk.Tk()

# Create a new Treeview widget
tree = ttk.Treeview(window, columns=('ID', 'Full Name', 'Team ID', 'Is Active', 'PTS'), show='headings')

# Set the column headings
tree.heading('ID', text='ID')
tree.heading('Full Name', text='Full Name')
tree.heading('Team ID', text='Team ID')
tree.heading('Is Active', text='Is Active')
tree.heading('PTS', text='PTS')


# Retrieve the data
c.execute("SELECT * FROM players")
rows = c.fetchall()

for row in rows:
    print(row)
    tree.insert('', 'end', values=row)

# Pack the Treeview to the window
tree.pack()

# Run the Tkinter event loop
window.mainloop()
# Close the connection
conn.close()