import telebot
from telebot import types
import os
import time

# === Токен берём из переменных окружения (чтобы не светить в коде) ===
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("❌ Не найден токен! Добавь переменную TOKEN в настройках Render или .env")

bot = telebot.TeleBot(TOKEN)

# === Список каналов ===
CHANNELS = [
    {"name": "🎬Фильмозавр - твой Кинозал🍿", "link": "https://t.me/filmozavrs"},
    # {"name": "📰 Анализатор", "link": "https://t.me/analyzer_news"},
    # {"name": "₿ Криптозавр", "link": "https://t.me/cryptozavr_channel"},
]

# === Команда /start ===
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_first_name = message.from_user.first_name or "друг"
    text = (
        f"🚀 Привет, {user_first_name}!\n\n"
        "Готов к погружению в мир кино, инфо-хайпа и криптовалютных волн?\n"
        "Тогда держись крепче — будет жарко! 🔥\n"
        "\n"
        "  🔴 Лучшие фильмы и сериалы всех времён 🍿🎬\n"
        "  🟡 Проверенные новости без воды 📰🤔\n"
        "  🟢 Крипто-выжимка 💶🫰\n\n"
        "Подпишись на наши главные каналы 👇"
    )
    
    markup = types.InlineKeyboardMarkup()
    for ch in CHANNELS:
        markup.add(types.InlineKeyboardButton(ch["name"], url=ch["link"]))
    
    bot.send_message(message.chat.id, text, reply_markup=markup)

# === Команда /channels ===
@bot.message_handler(commands=['channels'])
def show_channels(message):
    text = "📡 Наши актуальные каналы:\n\n"
    for ch in CHANNELS:
        text += f"{ch['name']} → {ch['link']}\n"
    bot.send_message(message.chat.id, text)

# === Запуск бота ===
def main():
    print("✅ Бот запущен и ждёт пользователей...")
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print("Ошибка:", e)
            time.sleep(5)

if __name__ == "__main__":
    main()
