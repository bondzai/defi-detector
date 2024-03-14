import os
import pandas as pd
from src.protocols import DefiProtocol
from src.constants.constants import USD_TO_THB

class Injective(DefiProtocol):
    def __init__(self, wallet_address):
        api_url = os.getenv("BLACK_API_URL")
        params = {"wallet_address": wallet_address}
        self.staking_balance = 2
        self.deposited = 90
        super().__init__(url=api_url, method="rest", **params)

    def fetch_price(self):
        self.url = "https://k8s.mainnet.asset.injective.network/asset-price/v1/coin/prices"
        df = pd.json_normalize(self.fetch_data_rest(), 'data')
        target = df[df['symbol'] == 'inj']
        if not target.empty:
            return float(target["current_price"].iloc[0])
        else:
            return 40

    def process_data(self):
        price = self.fetch_price()
        self.current_share_value = self.staking_balance * price
        message = "Injective\n\n"
        message += f"Staking Balance: {self.staking_balance} INJ, {self.current_share_value * USD_TO_THB:.2f} THB"
        if message:
            self.send_message(message, platforms=['line'])
