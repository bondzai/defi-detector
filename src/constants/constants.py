import os
from src.utils import Utils

USD_TO_THB = Utils.get_exchange_rate()

INITIAL_DEPOSITED = os.getenv("INITIAL_DEPOSITED").split(",")
BLACK_DEPOSITED = float(INITIAL_DEPOSITED[0])
BEEFY_DEPOSITED = float(INITIAL_DEPOSITED[1])
