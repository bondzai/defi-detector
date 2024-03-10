import requests
from bs4 import BeautifulSoup

class DefiProtocol:
    def __init__(self, url, method='rest', **params):
        self.url = url
        self.method = method
        self.params = params

    def fetch_data(self):
        if self.method == 'rest':
            return self.fetch_data_rest()
        elif self.method == 'webscrape':
            return self.fetch_data_webscrape()
        else:
            print("Error: Unsupported method specified.")
            return None

    def fetch_data_rest(self):
        response = requests.get(self.url, params=self.params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

    def fetch_data_webscrape(self):
        response = requests.get(self.url, params=self.params)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            data = {}
            data['title'] = soup.title.text
            return data
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
