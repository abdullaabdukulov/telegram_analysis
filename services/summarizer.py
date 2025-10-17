from collections import defaultdict
from utils.time import to_local_date
from domain.models import MessageData, ThreadSummary


def summarize_threads(threads: dict[int, list[MessageData]], timezone: str) -> dict[str, list[ThreadSummary]]:
    daily_summary = defaultdict(list)
    for thread_msgs in threads.values():
        date = to_local_date(thread_msgs[0].date, timezone)
        users = set(msg.sender_id for msg in thread_msgs)
        topic = thread_msgs[0].text[:30]
        summary = ThreadSummary(topic=topic, messages=len(thread_msgs), users=len(users))
        daily_summary[date].append(summary)
    return daily_summary
