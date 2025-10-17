import asyncio
from core.client import client
from core.fetcher import fetch_messages
from domain.models import MessageData
from domain.analyzer import extract_threads
from services.summarizer import summarize_threads
from utils.exporter import export_to_json
from config.settings import TIMEZONE


async def main():
    await client.start()
    raw_messages = await fetch_messages()
    messages = [
        MessageData(
            id=msg.id,
            sender_id=msg.sender_id,
            date=msg.date,
            text=msg.message,
            reply_to_msg_id=msg.reply_to_msg_id
        ) for msg in raw_messages
    ]
    threads = extract_threads(messages)
    summary = summarize_threads(threads, TIMEZONE)
    print(export_to_json(summary))
    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
