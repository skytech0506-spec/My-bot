from flask import Flask, request
import os
import requests

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.route('/')
def home():
    return "Bot Running - OK"

@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        
        reply = f"Neenga anupinathu: {text} 😊 Bot work aaguthu bro!"
        
        requests.post(f"{TELEGRAM_API}/sendMessage", json={
            "chat_id": chat_id,
            "text": reply
        })
    return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
