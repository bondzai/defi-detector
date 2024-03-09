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
            df_filtered = df[df['is_eol'] == False]
            print("Summary:")
            print(len(df_filtered))
        else:
            print("No data fetched.")
