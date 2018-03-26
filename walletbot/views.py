from flask import jsonify, request
from walletbot import app
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
        })

    raw_body = request.get_data()
    update = json.loads(raw_body)

    print(update)

    return jsonify({
        'message': 'ok'
    })
