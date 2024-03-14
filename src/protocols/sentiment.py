import pandas as pd
from src.protocols import DefiProtocol
from src.utils import Utils
from pprint import pprint

class Sentiment(DefiProtocol):
    def __init__(self):
        api_url = "https://api.alternative.me/fng/"
        params = {"limit": 1}
        super().__init__(api_url, **params)

    def process_data(self):
        print("Processing Sentiment data...", "\n")
        data = self.fetch_data()
        data = data.get("data", [])
        if data:
            df = pd.DataFrame(data)
            df["timestamp"] = df["timestamp"].apply(Utils.unix_to_humanreadable)
            df = df.drop(columns=["time_until_update"])
            pprint(df.to_dict(orient="records"))
        else:
            print("No data fetched.")
