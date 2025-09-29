#config.py
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Telegram Bot
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# GigaChat
GIGA_CHAT_TOKEN = os.getenv("GIGA_CHAT_TOKEN")  # Статический токен

# Database
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test_bot.db")

# Paths
BASE_DIR = Path(__file__).parent
DOWNLOAD_DIR = BASE_DIR / "temp"
DOWNLOAD_DIR.mkdir(exist_ok=True)

# Cache settings
CACHE_TTL = 3600  # 1 hour in seconds
MAX_CACHE_SIZE = 100  # Max files in cache

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Validation
if not TELEGRAM_TOKEN:
    raise ValueError("TELEGRAM_TOKEN not set in environment variables")
if not GIGA_CHAT_TOKEN:
    raise ValueError("GIGA_CHAT_TOKEN not set in environment variables")
