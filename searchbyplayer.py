from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players
import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# Get all players
nba_players = players.get_players()

def fetch_logs():
    # Get the player's name from the entry field
    player_name = name_entry.get()

    # Find the player
    player = [player for player in nba_players if player['full_name'] == player_name]
    
    if not player:
        messagebox.showerror("Error", "Player not found")
        return

    player = player[0]

    # Get game log for the player
    player_log = playergamelog.PlayerGameLog(player_id=player['id'])

    # Get the player's game logs
    logs = player_log.get_data_frames()[0]

    print(logs)

    # Calculate the player's total score
    total_score = logs['PTS'].sum()

    print(f"Player: {player['full_name']}, Score: {total_score}")

    # Clear the treeview
    for i in treeview.get_children():
        treeview.delete(i)

    # Define the columns
    treeview["columns"] = list(logs.columns)

    # Format the columns
    for column in logs.columns:
        treeview.column(column, width=100, minwidth=50)
        treeview.heading(column, text=column, anchor=tk.W)

    # Add the data to the treeview
    #for index, row in logs.iterrows():
    #   treeview.insert("", index, text=index, values=list(row))

    # Add the data to the treeview
    for index, row in logs.iterrows():
        # If the player scored more than a certain number of points, color the row green
        if row['PTS'] > 20:
            treeview.insert("", index, text=index, values=list(row), tags=('green',))
        else:
            treeview.insert("", index, text=index, values=list(row))

    # Hide the search view and show the results view
    search_frame.pack_forget()
    results_frame.pack()

def go_back():
    # Hide the results view and show the search view
    results_frame.pack_forget()
    search_frame.pack()

# Create a new tkinter window
window = tk.Tk()

# Create a frame for the search view
search_frame = tk.Frame(window)

# Create an entry field for the player's name
name_entry = tk.Entry(search_frame)
name_entry.pack()

# Create a button that fetches the game logs when clicked
fetch_button = tk.Button(search_frame, text="Fetch game logs", command=fetch_logs)
fetch_button.pack()

search_frame.pack()

# Create a frame for the results view
results_frame = tk.Frame(window)

# Create a new treeview
treeview = ttk.Treeview(results_frame)
treeview.pack(side='top', fill='both', expand=True)



# Color the rows with the 'green' tag
treeview.tag_configure('green', background='green')


# Create a button that goes back to the search view when clicked
back_button = tk.Button(results_frame, text="Back", command=go_back)
back_button.pack()

# Run the tkinter main loop
window.mainloop()