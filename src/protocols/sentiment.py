import pandas as pd
from src.protocols import DefiProtocol
from src.utils import Utils

class Sentiment(DefiProtocol):
    def __init__(self, *protocol_summaries):
        self.protocol_summaries = protocol_summaries
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

            print("Sentiment Data:")
            from pprint import pprint
            pprint(self.protocol_summaries)
            print()
            
            # for summary in self.protocol_summaries:
            #     print("****")
            #     print("Deposited:", summary["deposited"])
            #     print("Current Share Value:", summary["current_share_value"])

            message = "Market Sentiment\n\n"
            for _, row in df.iterrows():
                message += f"date: {row['timestamp']}\n"
                message += f"value: {row['value']} {row['value_classification']}\n"

            if message:
                self.send_message(message, platforms=['line'])
        else:
            print("No data fetched.")
