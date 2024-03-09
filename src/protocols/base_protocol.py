import requests

class DefiProtocol:
    def __init__(self, api_url, **params):
        self.api_url = api_url
        self.params = params

    def fetch_data(self):
        response = requests.get(self.api_url, params=self.params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
