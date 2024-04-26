from flask import Flask, request, jsonify

import socket

socket.getaddrinfo('cf31200.tw1.ru', port=8080)

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.json
    message = update.get('message')
    if message:
        text = message.get('text')
        chat_id = message.get('chat').get('id')
        sender = message.get('from').get('username')
        response_text = f"Hello, {sender}! You said: {text}"
        send_message(chat_id, response_text)
    return jsonify({'status': 'ok'})


def send_message(chat_id, text):
    # Function to send a message to Telegram using the Bot API
    # You need to implement this function
    pass  # Placeholder, implement your logic here


if __name__ == '__main__':
    app.run(host='cf31200.tw1.ru')
