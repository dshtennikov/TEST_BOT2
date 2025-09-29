#models.py
from sqlalchemy import Column, Integer, String, Text, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import pytz

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(BigInteger, unique=True, index=True, nullable=False)
    username = Column(String(100))
    first_name = Column(String(100))
    last_name = Column(String(100))
    created_at = Column(DateTime, default=lambda: datetime.now(pytz.UTC))

class Conversation(Base):
    __tablename__ = "conversations"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    user_message = Column(Text, nullable=False)
    bot_response = Column(Text, nullable=False)
    message_type = Column(String(20), default="text")  # text, document, photo
    file_info = Column(Text)  # Информация о файле, если есть
    created_at = Column(DateTime, default=lambda: datetime.now(pytz.UTC))

class FileCache(Base):
    __tablename__ = "file_cache"
    
    id = Column(Integer, primary_key=True, index=True)
    file_hash = Column(String(64), unique=True, index=True, nullable=False)
    file_path = Column(String(500), nullable=False)
    file_type = Column(String(50), nullable=False)
    extracted_text = Column(Text)
    created_at = Column(DateTime, default=lambda: datetime.now(pytz.UTC))
    accessed_at = Column(DateTime, default=lambda: datetime.now(pytz.UTC))
