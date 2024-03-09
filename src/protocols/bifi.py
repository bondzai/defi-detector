import os
import pandas as pd
from src.protocols import DefiProtocol
from pprint import pprint


class BeefyDataFetcher(DefiProtocol):
    def __init__(self, address):
        api_url = os.getenv("BEEFY_API_URL")
        params = {"address": address}
        super().__init__(api_url, **params)

    def process_data(self):
        response = self.fetch_data()
        if response:
            data = response

            df = pd.DataFrame(data)

            df_filtered = df[df['is_eol'] == False] 

            pprint(df_filtered.to_dict(orient="records"))
        else:
            print("No data fetched.")
