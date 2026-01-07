import telebot
import os

TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    print("BOT_TOKEN topilmadi")
    exit(1)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "Salom 👋\nQanday yordam bera olaman?"
    )

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)

print("Bot ishga tushdi...")
bot.infinity_polling()
