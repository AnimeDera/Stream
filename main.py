import os
from threading import Thread

def run_bot():
    # तुम्हारा bot start वाला code यहाँ होना चाहिए
    # example:
    # app.run_polling()
    pass

def run_web():
    from flask import Flask
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Bot is running!"

    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    Thread(target=run_bot).start()
    run_web()
