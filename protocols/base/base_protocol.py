import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_btoken_stats(wallet_address):
    url = f"https://blackpanther.fi/mainnet/api/btoken_stats?wallet_address={wallet_address}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Example usage:
wallet_address = os.getenv("INJ_ADDRESS")
btoken_stats = get_btoken_stats(wallet_address)

if btoken_stats:
    print(btoken_stats)
