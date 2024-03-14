import time

class Utils:
    @staticmethod
    def unix_to_humanreadable(unix_timestamp: int) -> str:
        """
        Converts a Unix timestamp to a human-readable YYYY-M-D-weekday format.
        """

        local_time = time.localtime(int(unix_timestamp))
        date_part = time.strftime("%Y-%m-%d", local_time)
        weekday = time.strftime("%A", local_time)  # Full weekday name
        return f"{date_part}-{weekday}"
