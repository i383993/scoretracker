import tkinter as tk
from tkinter import ttk
from nba_api.stats.static import teams

def fetch_data():
    # Get all NBA teams
    nba_teams = teams.get_teams()

    # Create a new tkinter window
    window = tk.Tk()

    # Create a new treeview
    treeview = ttk.Treeview(window)

    # Define the columns
    treeview["columns"]=("one","two","three")

    # Format the columns
    treeview.column("#0", width=270, minwidth=270, stretch=tk.NO)
    treeview.column("one", width=150, minwidth=150, stretch=tk.NO)
    treeview.column("two", width=400, minwidth=200)
    treeview.column("three", width=80, minwidth=50, stretch=tk.NO)

    # Define the column headings
    treeview.heading("#0",text="Name",anchor=tk.W)
    treeview.heading("one", text="ID",anchor=tk.W)
    treeview.heading("two", text="Full Name",anchor=tk.W)
    treeview.heading("three", text="Abbreviation",anchor=tk.W)

    # Add the data to the treeview
    for team in nba_teams:
        treeview.insert("", 0, text=team['nickname'], values=(team['id'], team['full_name'], team['abbreviation']))

    # Pack the treeview to the window
    treeview.pack(side='top', fill='both', expand=True)

    # Run the tkinter main loop
    window.mainloop()

fetch_data()