from dataclasses import dataclass
from datetime import datetime


@dataclass
class ThreadSummary:
    topic: str
    messages: int
    users: int


@dataclass
class MessageData:
    id: int
    sender_id: int
    date: datetime
    text: str
    reply_to_msg_id: int | None
