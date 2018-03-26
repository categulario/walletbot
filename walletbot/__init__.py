from flask import Flask, jsonify, request
import json


# Read config variables
app = Flask(__name__)
app.config.from_object('settings')
app.config.from_envvar('WALLETBOT_SETTINGS', silent=True)

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
