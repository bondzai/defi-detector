import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.protocols.black import Black
from protocols.beefy import Beefy
from dotenv import load_dotenv


def main():
    load_dotenv()

    beefy = Beefy(os.getenv("BEEFY_ADDRESS"))
    if beefy.fetch_data():
        beefy.process_data()

    black = Black(os.getenv("INJ_ADDRESS"))
    if black.fetch_data():
        black.process_data()

if __name__ == "__main__":
    main()
