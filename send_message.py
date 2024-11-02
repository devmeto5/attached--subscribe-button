from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application
import asyncio

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
bot_token = 'YOUR_BOT_TOKEN'

async def send_message():
    # Создаем клавиатуру с кнопкой "Подписаться"
    keyboard = [
        [InlineKeyboardButton("Подписаться", url="https://t.me/YourChannelUsername")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Создаем объект бота
    bot = Bot(token=bot_token)

    # Отправляем сообщение в канал
    await bot.send_message(
        chat_id='@YourChannelUsername',
        text="Присоединяйтесь к нашему каналу!",
        reply_markup=reply_markup
    )

if __name__ == "__main__":
    asyncio.run(send_message())
