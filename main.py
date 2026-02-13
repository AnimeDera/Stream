import os
from flask import Flask
from threading import Thread
from pyrogram import Client
from config import Config

# --------------------
# Flask App (Koyeb needs this)
# --------------------
app = Flask(__name__)

@app.route("/")
def home():
    return "AnimeDera Bot is Running"

# --------------------
# Telegram Bot
# --------------------
bot = Client(
    "animedera",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

@bot.on_message()
async def start(_, message):
    await message.reply_text("🤖 AnimeDera Bot Running on Koyeb")

def run_bot():
    bot.run()

# --------------------
# Start
# --------------------
if __name__ == "__main__":
    Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
