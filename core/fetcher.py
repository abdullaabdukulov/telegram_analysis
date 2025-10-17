from telethon.tl.types import Message
from datetime import datetime, timedelta
from core.client import client
from config.settings import GROUP_ID


async def fetch_messages(days: int = 7) -> list[Message]:
    end = datetime.utcnow()
    start = end - timedelta(days=days)
    messages = []
    async for msg in client.iter_messages(GROUP_ID, offset_date=end):
        if msg.date < start:
            break
        if msg.sender_id and msg.message:
            messages.append(msg)
    return messages
