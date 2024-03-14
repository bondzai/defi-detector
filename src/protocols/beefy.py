import os
import pandas as pd
from src.protocols import DefiProtocol
from src.constants.vault_constants import BEEFY_VAULT_ADDRESSES
from src.constants.constants import USD_TO_THB, BEEFY_DEPOSITED
from pprint import pprint

class Beefy(DefiProtocol):
    def __init__(self, address):
        api_url = os.getenv("BEEFY_API_URL")
        params = {"address": address}
        super().__init__(api_url, **params)

    def process_data(self):
        print("Processing Beefy data...", "\n")
        data = self.fetch_data()
        if data:
            df = pd.DataFrame(data)
            df = df[(df['is_eol'] == False) & (df['is_dashboard_eol'] == False)]
            df['datetime'] = pd.to_datetime(df['datetime'])
            df = df.sort_values(by='datetime', ascending=False)
            df = df.drop_duplicates(subset='product_key', keep='first')

            valid_product_keys = [key for key in BEEFY_VAULT_ADDRESSES.keys()]
            df = df[df['product_key'].isin(valid_product_keys)]

            df = df.drop(columns=[
                "is_eol",
                "is_dashboard_eol",
                "product_key",
                "transaction_hash",
            ])

            # print("Summary:")
            # pprint(df.to_dict(orient="records"))
            current_share_value = float(os.getenv("BEEFY_VALUE"))
            accumulated_pnl = current_share_value - BEEFY_DEPOSITED
            accumulated_performance = ((current_share_value - BEEFY_DEPOSITED) / BEEFY_DEPOSITED) * 100 if BEEFY_DEPOSITED > 0 else 0

            message = "Beefy\n\n"
            message += (
                f"Deposited {BEEFY_DEPOSITED:.2f} USD, {BEEFY_DEPOSITED * USD_TO_THB:.2f} THB\n"
                f"Current: {current_share_value:.2f} USD, {current_share_value * USD_TO_THB:.2f} THB\n"
                f"Acc PNL: {accumulated_pnl:.2f} USD, {accumulated_pnl * USD_TO_THB:.2f} THB\n"
                f"Acc %PNL {accumulated_performance:.2f}%\n"
            )
            if message:
                self.send_message(message, platforms=['line'])
        else:
            print("No data fetched.")
