import os
from dotenv import load_dotenv

load_dotenv()

DEV_ID = int(os.getenv("DEVELOPER_USER_ID"))
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN_DEV")
GROQ_TOKEN = os.getenv("GROQ_API_KEY")