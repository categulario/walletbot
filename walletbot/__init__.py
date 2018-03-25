from flask import Flask, jsonify


# Read config variables
app = Flask(__name__)
app.config.from_object('settings')
app.config.from_envvar('WALLETBOT_SETTINGS', silent=True)

@app.route('/')
def hello():
    return jsonify({
        'message': 'Hello, my name is walletbot'
    })
