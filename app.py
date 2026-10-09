from flask import Flask, request
import telegram
import os

TOKEN = "8829216356:AAEk2fXgwa5MsONMGbKbv4Jygir9dE9dqGc"
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text
    bot.send_message(chat_id=chat_id, text=f"Neenga anupinathu: {text}")
    return 'ok'

@app.route('/')
def home():
    return 'Bot Running - OK'

if __name__ == '__main__':
    app.run(port=10000)
