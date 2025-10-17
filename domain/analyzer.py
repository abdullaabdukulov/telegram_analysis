from collections import defaultdict
from domain.models import MessageData


def extract_threads(messages: list[MessageData]) -> dict[int, list[MessageData]]:
    threads = defaultdict(list)
    for msg in messages:
        key = msg.reply_to_msg_id or msg.id
        threads[key].append(msg)
    return threads
