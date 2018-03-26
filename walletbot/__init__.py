from flask import Flask


# Read config variables
app = Flask(__name__)
app.config.from_object('settings')
app.config.from_envvar('WALLETBOT_SETTINGS', silent=True)

import walletbot.views
