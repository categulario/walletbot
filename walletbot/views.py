from flask import jsonify, request
from walletbot import app
from walletbot.mongo import client
import json


@app.route('/')
def hello():
    return jsonify({
        'message': 'Hello, my name is walletbot'
    })

@app.route('/webhook/<token>', methods=['POST'])
def telegram_webhook(token):
    if token != app.config['TELEGRAM_AUTH_TOKEN']:
        return jsonify({
            'ok': False,
            'error_code': 400,
            'description': 'Bad Request: wrong telegram auth token',
        }), 400

    raw_body = request.get_data()
    update = json.loads(raw_body)

    query = client.messages.insert_one(update)

    return jsonify({
        'message': 'ok'
    })
