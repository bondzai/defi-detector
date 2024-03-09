import os
import pandas as pd
from src.protocols.base_protocol import DefiProtocol


class BlackDataFetcher(DefiProtocol):
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
