from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players
import pandas as pd
import tkinter as tk
from tkinter import ttk

# Get all players
nba_players = players.get_players()

# Find a specific player
player = [player for player in nba_players if player['full_name'] == 'Jayson Tatum'][0] 

# Get game log for the player
player_log = playergamelog.PlayerGameLog(player_id=player['id'])

# Get the player's game logs
logs = player_log.get_data_frames()[0]

print(logs)

# Calculate the player's total score
total_score = logs['PTS'].sum()

print(f"Player: {nba_players[0]['full_name']}, Score: {total_score}")

# Create a new tkinter window
window = tk.Tk()

# Create a new treeview
treeview = ttk.Treeview(window)

# Define the columns
treeview["columns"] = list(logs.columns)

# Format the columns
for column in logs.columns:
    treeview.column(column, width=100, minwidth=50, stretch=tk.NO)
    treeview.heading(column, text=column, anchor=tk.W)

# Add the data to the treeview
for index, row in logs.iterrows():
    treeview.insert("", index, text=index, values=list(row))

# Pack the treeview to the window
treeview.pack(side='top', fill='both', expand=True)

# Run the tkinter main loop
window.mainloop()