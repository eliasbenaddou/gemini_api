import time
from datetime import datetime


def date_to_unix_ts(date: str) -> int:
    timestamp_obj = datetime.strptime(date, "%Y%m%d").timetuple()
    unix_ts = int(time.mktime(timestamp_obj))

    return unix_ts
