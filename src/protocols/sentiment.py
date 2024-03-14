import pandas as pd
from src.protocols import DefiProtocol
from pprint import pprint
import time

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
            df["timestamp"] = df["timestamp"].apply(self.unix_to_humanreadable)
            df = df.drop(columns=["time_until_update"])
            pprint(df.to_dict(orient="records"))
        else:
            print("No data fetched.")

    def unix_to_humanreadable(self, unix_timestamp:int):
        local_time = time.localtime(int(unix_timestamp))

        # Format date in YYYY-M-D format
        date_part = time.strftime("%Y-%m-%d", local_time)

        # Get weekday name using strftime("%A") or "%a" for short name
        weekday = time.strftime("%A", local_time)  # Full weekday name (e.g., Wednesday)
        # weekday = time.strftime("%a", local_time)  # Short weekday name (e.g., Wed)

        # Combine date and weekday
        human_readable_time = f"{date_part}-{weekday}"

        return human_readable_time
