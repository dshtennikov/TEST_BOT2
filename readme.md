# Telegram Bot - Ассистент по Microsoft Office

🤖 Умный Telegram бот, помогающий студентам и менеджерам с вопросами по Microsoft Office. Использует GigaChat API для интеллектуальных ответов и обрабатывает различные типы файлов.

## ✨ Возможности

- **💬 Умные ответы** - Интеграция с GigaChat для контекстных ответов по Microsoft Office
- **📁 Обработка файлов** - Поддержка PDF, DOCX, XLSX и изображений
- **🖼️ Распознавание текста** - OCR для изображений и сканированных PDF
- **💾 История диалогов** - Сохранение контекста разговоров
- **⚡ Кэширование** - Интеллектуальное кэширование обработанных файлов
- **🔍 Поиск по истории** - Команда для просмотра предыдущих диалогов

## 🛠 Технологии

- `python-telegram-bot` - Telegram Bot API
- `GigaChat API` - Модель искусственного интеллекта
- `SQLAlchemy` - Работа с базой данных
- `PyMuPDF` - Обработка PDF
- `python-docx` - Работа с Word документами
- `openpyxl` - Обработка Excel файлов
- `pytesseract` - OCR распознавание текста
- `Pillow` - Обработка изображений

## 📦 Установка

### 1. Клонирование репозитория

```bash
git clone https://github.com/your-username/office-assistant-bot.git
cd office-assistant-bot

pip install -r requirements.txt

# Скачать и установить с https://github.com/UB-Mannheim/tesseract/wiki
# Добавить в PATH: C:\Program Files\Tesseract-OCR\

sudo apt update
sudo apt install tesseract-ocr
sudo apt install tesseract-ocr-rus

