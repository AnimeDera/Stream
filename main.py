import os
from flask import Flask
from threading import Thread
from pyrogram import Client
from config import Config

# -----------------------------
# Telegram Bot Setup
# -----------------------------

bot = Client(
    "premium-bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

@bot.on_message()
async def start_handler(client, message):
    await message.reply_text("🔥 Premium Bot is Running!")

# -----------------------------
# Web Server (Koyeb ke liye)
# -----------------------------

web_app = Flask(__name__)

@web_app.route("/")
def home():
    return "Bot is running!"

def run_web():
    port = int(os.environ.get("PORT", 8000))
    web_app.run(host="0.0.0.0", port=port)

# -----------------------------
# Start Both
# -----------------------------

if __name__ == "__main__":
    Thread(target=run_web).start()
    bot.run()
