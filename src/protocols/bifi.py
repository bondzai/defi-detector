import os
import pandas as pd
from src.protocols import DefiProtocol


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
            df_sorted = df.sort_values(by='datetime', ascending=False)
            df_filtered = df_sorted.drop_duplicates(subset='product_key', keep='first')

            print(df_filtered)
            print("Summary:")
            print(len(df_filtered))

            from pprint import pprint
            pprint(df_filtered.to_dict(orient="records"))
        else:
            print("No data fetched.")
