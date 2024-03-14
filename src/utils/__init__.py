import time

class Utils:
    @staticmethod
    def unix_to_humanreadable(unix_timestamp: int) -> str:
        """
        Converts a Unix timestamp to a human-readable YYYY-M-D format.
        """

        local_time = time.localtime(int(unix_timestamp))
        return time.strftime("%Y-%m-%d", local_time)
