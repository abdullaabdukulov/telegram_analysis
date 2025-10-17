import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION_NAME = os.getenv("SESSION_NAME", "telegram_analysis")
GROUP_ID = int(os.getenv("GROUP_ID"))
TIMEZONE = os.getenv("TIMEZONE", "Asia/Tashkent")
