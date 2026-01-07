import telebot
import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

TOKEN = os.environ.get("BOT_TOKEN")
PORT = int(os.environ.get("PORT", 4000))

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom 👋\nQanday yordam bera olaman?")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, m.text)

# ----- FAKE WEB SERVER -----
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")

def run_server():
    server = HTTPServer(("", PORT), SimpleHandler)
    server.serve_forever()

threading.Thread(target=run_server).start()

print("Bot ishga tushdi...")
bot.infinity_polling()
