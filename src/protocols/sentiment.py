import pandas as pd
from src.protocols import DefiProtocol
from src.utils import Utils
from src.constants.constants import USD_TO_THB


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

            message = "Portfolio\n\n"
            self.deposited = 0
            self.current_share_value = 0

            for proto in self.protocol_summaries:
                if proto["is_enable"]:
                    self.deposited += proto["deposited"]
                    self.current_share_value += proto["current_share_value"]

            message += f"Deposited: {self.deposited * USD_TO_THB:.2f} THB\n"
            message += f"Current: {self.current_share_value * USD_TO_THB:.2f} THB\n"
            message += f"PNL: {(self.current_share_value - self.deposited) * USD_TO_THB:.2f} THB\n"
            message += f"%PNL: {((self.current_share_value - self.deposited) / self.deposited) * 100:.2f}%\n"

            if message:
                self.send_message(message, platforms=['line', 'discord'])

            message = "\n\n"
            for _, row in df.iterrows():
                message += f"date: {row['timestamp']}\n"
                message += f"value: {row['value']} {row['value_classification']}\n"

            if message:
                self.send_message(message, platforms=['line', 'discord'])
        else:
            print("No data fetched.")
