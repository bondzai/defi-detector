import os
import pandas as pd
from src.protocols import DefiProtocol

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
        print("Processing Injective data...", "\n")
        price = self.fetch_price()
        self.current_share_value = self.staking_balance * price
