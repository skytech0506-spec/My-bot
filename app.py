from flask import Flask, request
import telegram

TOKEN = "8829216356:AAEk2fXgwa5MsONMGbKbv4Jygir9dE9dqGc"
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    try:
        data = request.get_json(force=True)
        update = telegram.Update.de_json(data, bot)
        if update.message:
            chat_id = update.message.chat.id
            text = update.message.text
            bot.send_message(chat_id=chat_id, text=f"Neenga anupinathu: {text}")
    except Exception as e:
        print(e)
    return 'ok'

@app.route('/')
def home():
    return 'Bot Running - OK'

if __name__ == '__main__':
    app.run(port=10000, host='0.0.0.0')
