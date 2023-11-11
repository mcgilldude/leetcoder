import requests

url = "https://realtor.p.rapidapi.com/locations/v2/auto-complete"

querystring = {"input":"new york","limit":"10"}

headers = {
	"X-RapidAPI-Key": "b5cc6e6cb5msh34825b15e6ce694p129f6ajsncb3ebe00060c",
	"X-RapidAPI-Host": "realtor.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())