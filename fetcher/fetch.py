import requests

def fetch_data():
    url = "https://us500.com/data/globalMin.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["data"]