import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://fbref.com/en/squads/19538871/Manchester-United-Stats#all_matchlog"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the element containing the goals for and goals against information
    goals_table = soup.find('table', {'id': 'all_matchlog'})

    # Check if the table is found
    if goals_table:
        # Extract goals for and goals against
        goals_for = goals_table.find('td', {'data-stat': 'goals_for'}).text.strip()
        goals_against = goals_table.find('td', {'data-stat': 'goals_against'}).text.strip()

        # Create a Pandas DataFrame
        data = {'Goals For': [goals_for], 'Goals Against': [goals_against]}
        df = pd.DataFrame(data)

        # Print the DataFrame
        print(df)

    else:
        print("Goals table not found on the page.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
