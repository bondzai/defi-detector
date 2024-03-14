import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.protocols.black import Black
from src.protocols.beefy import Beefy
from src.protocols.injective import Injective
from src.protocols.sentiment import Sentiment
from dotenv import load_dotenv


def main():
    load_dotenv()
    inj_address = os.getenv("INJ_ADDRESS")
    evm_address = os.getenv("EVM_ADDRESS")

    beefy = Beefy(evm_address)
    if beefy.fetch_data():
        beefy.process_data()

    print("****")
    print(beefy.deposited)
    print(beefy.current_share_value)

    black = Black(inj_address)
    if black.fetch_data():
        black.process_data()

    print("****")
    print(black.deposited)
    print(black.current_share_value)

    injective = Injective(inj_address)
    injective.process_data()

    print("****")
    print(injective.deposited)
    print(injective.current_share_value)

    sentiment = Sentiment()
    sentiment.process_data()

if __name__ == "__main__":
    main()
