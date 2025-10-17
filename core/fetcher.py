from telethon.tl.types import Message
from datetime import datetime, timedelta, timezone
from core.client import client
from config.settings import GROUP_ID


async def fetch_messages(days: int = 7) -> list[Message]:
    end = datetime.now(timezone.utc)
    start = end - timedelta(days=days)
    messages = []

    entity = await client.get_input_entity(GROUP_ID)

    async for msg in client.iter_messages(entity, offset_date=end):
        if msg.date < start:
            break
        if msg.sender_id and msg.message:
            messages.append(msg)
    return messages
