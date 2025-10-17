from pytz import timezone as tz
from datetime import datetime


def to_local_date(dt: datetime, tz_name: str) -> str:
    return dt.astimezone(tz(tz_name)).date().isoformat()
