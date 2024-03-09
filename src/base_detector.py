import requests

class BaseDefiDetector:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get_data(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None
