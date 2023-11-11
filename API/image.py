import requests
from datetime import datetime

def get_nasa_apod(api_key):
    base_url = "https://api.nasa.gov/planetary/apod"
    params = {
        'api_key': api_key,
        'hd': True  # Set to True for high-resolution image
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def display_apod(apod_data):
    if apod_data:
        title = apod_data['title']
        date = apod_data['date']
        explanation = apod_data['explanation']
        media_type = apod_data['media_type']

        print(f"\nNASA Astronomy Picture of the Day ({date})")
        print(f"Title: {title}")
        print(f"Explanation: {explanation}")

        if media_type == 'image':
            url = apod_data['url']
            print(f"\nImage URL: {url}")
        elif media_type == 'video':
            url = apod_data['url']
            print(f"\nVideo URL: {url}")
        else:
            print("\nUnsupported media type.")

    else:
        print("Failed to fetch NASA Astronomy Picture of the Day.")

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual NASA API key
    api_key = 'YOUR_API_KEY'

    apod_data = get_nasa_apod(api_key)

    # Display APOD information
    display_apod(apod_data)
