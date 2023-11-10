import requests
from bs4 import BeautifulSoup

url = "https://fbref.com/en/squads/19538871/Manchester-United-Stats#all_matchlogs"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the element containing the fixture information
    fixtures_table = soup.find('table', {'id': 'all_matchlogs'})

    # Check if the table is found
    if fixtures_table:
        # Extract and print the fixture information (you may need to adjust the code based on the actual structure of the table)
        rows = fixtures_table.find_all('tr', class_='full_width')
        for row in rows:
            date = row.find('td', {'data-stat': 'date'}).text.strip()
            home_team = row.find('td', {'data-stat': 'squad_a'}).text.strip()
            away_team = row.find('td', {'data-stat': 'squad_b'}).text.strip()

            print(f"{date}: {home_team} vs {away_team}")

    else:
        print("Fixtures table not found on the page.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
