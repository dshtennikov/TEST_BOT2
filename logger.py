#logger.py
import logging
import sys
from pathlib import Path
from config import LOG_LEVEL, LOG_FORMAT, BASE_DIR

def setup_logger():
    """Настройка логирования для всего проекта"""
    
    # Создаем логгер
    logger = logging.getLogger("telegram_bot")
    logger.setLevel(getattr(logging, LOG_LEVEL))
    
    # Форматтер
    formatter = logging.Formatter(LOG_FORMAT)
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler
    log_file = BASE_DIR / "telegram_bot.log"
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    # Настройка логирования для внешних библиотек
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("telegram").setLevel(logging.WARNING)
    
    return logger

# Глобальный логгер
logger = setup_logger()
