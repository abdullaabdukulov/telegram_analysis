import json
from config.settings import TIMEZONE
from domain.models import ThreadSummary


def export_to_json(summary: dict[str, list[ThreadSummary]]) -> str:
    return json.dumps({
        "timezone": TIMEZONE,
        "days": [
            {
                "date": date,
                "threads": sorted(
                    [
                        {
                            "topic": thread.topic,
                            "messages": thread.messages,
                            "users": thread.users
                        } for thread in threads
                    ],
                    key=lambda x: x["messages"],
                    reverse=True
                )
            } for date, threads in sorted(summary.items())
        ]
    }, ensure_ascii=False, indent=2)
