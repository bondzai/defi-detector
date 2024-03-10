import os
import pandas as pd
from src.protocols import DefiProtocol
from src.constants.constants import USD_TO_THB

class Injective(DefiProtocol):
    def __init__(self, wallet_address):
        api_url = os.getenv("BLACK_API_URL")
        params = {"wallet_address": wallet_address}
        self.staking_balance = 2
        super().__init__(url=api_url, method="rest", **params)

    def process_data(self):
        print("Processing Injective data...", "\n")
        print(f"Staking Balance: {self.staking_balance} INJ, {self.staking_balance * 1450} THB")
