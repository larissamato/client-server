from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from datetime import datetime
import pusher
import logging
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

logging.basicConfig(level=logging.DEBUG)

# Inicialização do Pusher
pusher_client = pusher.Pusher(
    app_id=os.getenv('PUSHER_APP_ID'),
    key=os.getenv('PUSHER_KEY'),
    secret=os.getenv('PUSHER_SECRET'),
    cluster=os.getenv('PUSHER_CLUSTER'),
    ssl=True
)

clients = {}

@app.route('/message', methods=['POST'])
def post_message():
    try:
        data = request.json
        username = data.get('username')
        port = data.get('port')
        message = data.get('message')

        timestamp = datetime.now().strftime('%H:%M:%S')
        formatted_message = f"{timestamp} - {username} - {port}: {message}"

        pusher_client.trigger(u'chat-channel', u'new-message', {u'message': message, u'time': timestamp, u'username': username, u'port': port})

        return jsonify({'status': 'success!!'}), 200
    except Exception as e:
        logging.error(f"Erro ao enviar mensagem: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/join', methods=['POST'])
def post_join():
    try:
        data = request.json
        username = data.get('username')
        port = data.get('port')
        client_ip = request.remote_addr

        clients[username] = {'port': port, 'ip': client_ip}
        notify_users(f"{username} entrou no chat.", "join")

        return jsonify({'status': 'joined'}), 200
    except Exception as e:
        logging.error(f"Erro ao conectar: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/leave', methods=['POST'])
def post_leave():
    try:
        data = request.json
        username = data.get('username')

        if username in clients:
            del clients[username]
            notify_users(f"{username} saiu do chat.", "leave")

        return jsonify({'status': 'left'}), 200
    except Exception as e:
        logging.error(f"Erro ao sair: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

def notify_users(message, action):
    try:
        logging.debug(f"Notificando usuários: {message}")
        pusher_client.trigger('chat-channel', 'new-message', {'message': message, 'action': action})
    except Exception as e:
        logging.error(f"Erro ao notificar: {e}")

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'status': 'server is running, pong'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT', 5000))
