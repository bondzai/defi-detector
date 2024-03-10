import requests

class DefiProtocol:
    def __init__(self, url, **params):
        self.url = url
        self.params = params

    def fetch_data(self):
        response = requests.get(self.url, params=self.params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
