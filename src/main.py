import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from protocols.black_panther import BlackDataFetcher
from protocols.bifi import BeefyDataFetcher
from dotenv import load_dotenv


def main():
    load_dotenv()

    bifi = BeefyDataFetcher(os.getenv("BEEFY_ADDRESS"))
    data = bifi.fetch_data()
    if data:
        print("bifi ok")

    black = BlackDataFetcher(os.getenv("INJ_ADDRESS"))
    data = black.fetch_data()
    if data:
        print("black ok")
        black.process_data()

if __name__ == "__main__":
    main()
