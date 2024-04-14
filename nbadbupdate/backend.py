import pandas as pd
import requests
import json
import sqlite3

BASE_URL = "http://api.balldontlie.io"
ALL_JSON = "/v1/games"

# Define the query parameters
params = {
    'dates[]': ['2024-04-05']
}

# Define headers
headers = {
    'Authorization': 'dcbe01ca-2080-4356-b44a-b52f95aae369'
}

# Send the GET request with the query parameters and headers
response = requests.get(BASE_URL + ALL_JSON, params=params, headers=headers)

# Initialize an empty DataFrame with the desired column names
df = pd.DataFrame(columns=['home_team', 'home_score', 'visitor_team', 'visitor_score'])

# Check if the response is valid
if response.status_code == 200:
    data = json.loads(response.text)

    # Loop through the data and extract the team names and scores
    for game in data['data']:
        home_team = game['home_team']['full_name']
        visitor_team = game['visitor_team']['full_name']
        home_score = game['home_team_score']
        visitor_score = game['visitor_team_score']

        # Create a new DataFrame row and append it to the existing DataFrame
        new_row = pd.DataFrame([[home_team, home_score, visitor_team, visitor_score]], columns=df.columns)
        df = pd.concat([df, new_row], ignore_index=True)

# Create a connection to the SQLite database
conn = sqlite3.connect('games.db')

# Write the DataFrame to the SQLite database
df.to_sql('nba', conn, if_exists='replace', index=False)

# Close the connection to the SQLite database
conn.close()