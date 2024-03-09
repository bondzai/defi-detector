from src.protocols.base_protocol import ProtocolDataFetcher
import pandas as pd
import os

class BeefyDataFetcher(ProtocolDataFetcher):
    def __init__(self, address):
        api_url = os.getenv("BEEFY_API_URL")
        params = {"address": address}
        super().__init__(api_url, **params)
