import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from protocols.black_panther import BlackDataFetcher
from protocols.beefy import BeefyDataFetcher
from dotenv import load_dotenv


def main():
    load_dotenv()

    bifi = BeefyDataFetcher(os.getenv("BEEFY_ADDRESS"))
    if bifi.fetch_data():
        bifi.process_data()

    black = BlackDataFetcher(os.getenv("INJ_ADDRESS"))
    if black.fetch_data():
        black.process_data()

if __name__ == "__main__":
    main()
