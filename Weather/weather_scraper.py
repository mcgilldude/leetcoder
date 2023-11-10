import requests
from bs4 import BeautifulSoup

def get_weather_data(city):
    # Replace the URL with the actual URL of the weather website you want to scrape
    url = f'https://www.weather-forecast.com/locations/{city}/forecasts/latest'
    
    try:
        # Send an HTTP request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the weather information
        weather_info = soup.find('span', class_='temp').text.strip()

        return weather_info
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    city_name = input("Enter the name of the city for weather information: ")
    weather_data = get_weather_data(city_name)

    if weather_data:
        print(f"Weather in {city_name}: {weather_data}")
    else:
        print("Failed to retrieve weather information.")
