import os
from dotenv import load_dotenv
import requests
import pandas as pd

class ProtocolDataFetcher:
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

class BeefyDataFetcher(ProtocolDataFetcher):
    def __init__(self, address):
        api_url = os.getenv("BEEFY_API_URL")
        params = {"address": address}
        super().__init__(api_url, **params)

class BlackDataFetcher(ProtocolDataFetcher):
    def __init__(self, wallet_address):
        api_url = os.getenv("BLACK_API_URL")
        params = {"wallet_address": wallet_address}
        super().__init__(api_url, **params)

    def process_data(self):
        data = self.fetch_data()
        if data:
            df = pd.DataFrame(data)
            total_previous_share_value = df['previous_share_value'].sum()
            total_current_share_value = df['current_share_value'].sum()
            total_performance = df['performance'].sum() / len(df) if len(df) > 0 else 0

            print("Summary:")
            print(f"Previous Share Value: {total_previous_share_value:.2f}")
            print(f"Current Share Value: {total_current_share_value:.2f}")
            print(f"Performance: {total_performance:.2f}%")
        else:
            print("No data fetched.")

# Example usage
if __name__ == "__main__":
    load_dotenv()

    bifi = BeefyDataFetcher(os.getenv("BEEFY_ADDRESS"))
    data = bifi.fetch_data()
    if data:
        print("bifi ok")

    black = BlackDataFetcher(os.getenv("INJ_ADDRESS"))
    data = black.fetch_data()
    if data:
        print("black ok")
        black.process_data()
