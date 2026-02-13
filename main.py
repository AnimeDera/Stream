from telethon import TelegramClient, events
from config import Config

bot = TelegramClient('headmaster', Config.API_ID, Config.API_HASH).start(bot_token=Config.BOT_TOKEN)

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply("जी बॉस! हेडmaster सिस्टम तैयार है।")

print("बोट शुरू हो गया है, बॉस...")
bot.run_until_disconnected()