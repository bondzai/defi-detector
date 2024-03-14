import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dotenv import load_dotenv
from src.protocols.black import Black
from src.protocols.beefy import Beefy
from src.protocols.injective import Injective
from src.protocols.sentiment import Sentiment

def main():
    load_dotenv()
    inj_address = os.getenv("INJ_ADDRESS")
    evm_address = os.getenv("EVM_ADDRESS")

    protocols = [
        {"class": Beefy, "args": (evm_address,)},
        {"class": Black, "args": (inj_address,)},
        {"class": Injective, "args": (inj_address,)}
    ]

    protocol_summaries = [summarize_protocol_data(proto["class"], *proto["args"]) for proto in protocols]

    sentiment = Sentiment(*protocol_summaries)
    sentiment.process_data()

def summarize_protocol_data(protocol_class, *args):
    protocol_instance = protocol_class(*args)
    if protocol_instance.fetch_data():
        protocol_instance.process_data()
        return {
            "deposited": protocol_instance.deposited,
            "current_share_value": protocol_instance.current_share_value
        }
    else:
        return {
            "deposited": None,
            "current_share_value": None
        }

if __name__ == "__main__":
    main()
