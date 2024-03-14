import os
import pandas as pd
from src.protocols import DefiProtocol
from src.constants.vault_constants import BLACK_VAULT_ADDRESSES
from src.constants.constants import USD_TO_THB, BLACK_DEPOSITED

class Black(DefiProtocol):
    def __init__(self, wallet_address):
        api_url = os.getenv("BLACK_API_URL")
        params = {"wallet_address": wallet_address}
        super().__init__(url=api_url, method="rest", **params)

    def process_data(self):
        print("Processing Black data...\n")
        data = self.fetch_data()
        if data:
            df = pd.DataFrame(data)
            df['vault_address_mapped'] = df['vault_address'].map(BLACK_VAULT_ADDRESSES)
            grouped_data = df.groupby('vault_address_mapped').agg(
                total_previous_share_value=('previous_share_value', 'sum'),
                total_current_share_value=('current_share_value', 'sum'),
                total_performance=('performance', lambda x: x.sum() / len(x) if len(x) > 0 else 0)
            )

            message = "Black\n\n"
            for index, row in grouped_data.iterrows():
                message += (
                    f"{index}\n"
                    f"Previous: {row['total_previous_share_value']:.2f}\n"
                    f"Current: {row['total_current_share_value']:.2f}\n"
                    f"PNL: {row['total_current_share_value'] - row['total_previous_share_value']:.2f}\n"
                    f"%PNL: {row['total_performance']:.2f}%\n\n"
                )

            previous_share_value = df['previous_share_value'].sum()
            current_share_value = df['current_share_value'].sum()
            pnl = current_share_value - previous_share_value 
            performance = ((current_share_value - previous_share_value) / previous_share_value) * 100 if previous_share_value > 0 else 0
            accumulated_pnl = current_share_value - BLACK_DEPOSITED
            accumulated_performance = ((current_share_value - BLACK_DEPOSITED) / BLACK_DEPOSITED) * 100 if BLACK_DEPOSITED > 0 else 0

            message += (
                f"Summary:\n"
                f"Previous: {previous_share_value:.2f} USD, {previous_share_value * USD_TO_THB:.2f} THB\n"
                f"Current: {current_share_value:.2f} USD, {current_share_value * USD_TO_THB:.2f} THB\n"
                f"PNL: {pnl:.2f} USD, {pnl * USD_TO_THB:.2f} THB\n"
                f"%PNL: {performance:.2f}%\n\n"
                f"Deposited {BLACK_DEPOSITED:.2f} USD, {BLACK_DEPOSITED * USD_TO_THB:.2f} THB\n"
                f"Acc PNL: {accumulated_pnl:.2f} USD, {accumulated_pnl * USD_TO_THB:.2f} THB\n"
                f"Acc %PNL {accumulated_performance:.2f}%\n"
            )


            if message:
                self.send_message(message, platforms=['line'])
        else:
            print("No data fetched.")