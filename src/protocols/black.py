import os
import pandas as pd
from src.protocols import DefiProtocol
from src.constants.vault_constants import BLACK_VAULT_ADDRESSES

class Black(DefiProtocol):
    def __init__(self, wallet_address):
        api_url = os.getenv("BLACK_API_URL")
        params = {"wallet_address": wallet_address}
        super().__init__(api_url, **params)

    def process_data(self):
        print("Processing Black data...", "\n")
        data = self.fetch_data()
        if data:
            df = pd.DataFrame(data)

            df['vault_address_mapped'] = df['vault_address'].map(BLACK_VAULT_ADDRESSES)

            grouped_data = df.groupby('vault_address_mapped').agg(
                total_previous_share_value=('previous_share_value', 'sum'),
                total_current_share_value=('current_share_value', 'sum'),
                total_performance=('performance', lambda x: x.sum() / len(x) if len(x) > 0 else 0)
            )

            for index, row in grouped_data.iterrows():
                print(f"Vault Strategy: {index}")
                print(f"Previous Share Value: {row['total_previous_share_value']:.2f}")
                print(f"Current Share Value: {row['total_current_share_value']:.2f}")
                print(f"Performance: {row['total_performance']:.2f}%")
                print()

            total_previous_share_value = df['previous_share_value'].sum()
            total_current_share_value = df['current_share_value'].sum()
            total_performance = df['performance'].sum() / len(df) if len(df) > 0 else 0

            print("Summary:")
            print(f"Previous Share Value: {total_previous_share_value:.2f}")
            print(f"Current Share Value: {total_current_share_value:.2f}")
            print(f"Performance: {total_performance:.2f}%")
            print()
        else:
            print("No data fetched.")
