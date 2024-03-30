import time
import os
import requests

class Utils:
    @staticmethod
    def unix_to_humanreadable(unix_timestamp: int) -> str:
        """
        Converts a Unix timestamp to a human-readable YYYY-M-D format.
        """

        local_time = time.localtime(int(unix_timestamp))
        return time.strftime("%Y-%m-%d", local_time)

    @staticmethod
    def get_exchange_rate():
        """
        Fetches the exchange rate from the provided API URL.
        """
        api_url = os.getenv("EXCHANGE_RATE_API_URL")
        if not api_url:
            raise ValueError("EXCHANGE_RATE_API_URL environment variable is not set.")

        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
            exchange_rate = data.get("rates").get("THB")
            if exchange_rate is None:
                raise ValueError("Exchange rate not found in API response.")
            return exchange_rate
        except requests.RequestException as e:
            raise ValueError(f"Failed to fetch exchange rate: {e}")
