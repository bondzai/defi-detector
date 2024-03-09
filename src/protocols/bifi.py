import os
import pandas as pd
from src.protocols import DefiProtocol
from src.constants.vault_constants import BIFI_VAULT_ADDRESSES
from pprint import pprint

class BeefyDataFetcher(DefiProtocol):
    def __init__(self, address):
        api_url = os.getenv("BEEFY_API_URL")
        params = {"address": address}
        super().__init__(api_url, **params)

    def process_data(self):
        data = self.fetch_data()
        if data:
            df = pd.DataFrame(data)
            df = df[(df['is_eol'] == False) & (df['is_dashboard_eol'] == False)]
            df['datetime'] = pd.to_datetime(df['datetime'])
            df = df.sort_values(by='datetime', ascending=False)
            df = df.drop_duplicates(subset='product_key', keep='first')

            valid_product_keys = [key for key in BIFI_VAULT_ADDRESSES.keys()]
            df = df[df['product_key'].isin(valid_product_keys)]

            df = df.drop(columns=[
                "is_eol",
                "is_dashboard_eol",
                "product_key",
                "transaction_hash",
            ])

            print("Summary:")
            pprint(df.to_dict(orient="records"))
        else:
            print("No data fetched.")
