pidfile        = '/run/gunicorn/walletbot.pid'
bind           = ['0.0.0.0:5000']
user           = 'www-data'
group          = 'www-data'
accesslog      = '/var/log/gunicorn/walletbot.access.log'
errorlog       = '/var/log/gunicorn/walletbot.error.log'
raw_env        = ['WALLETBOT_SETTINGS=/home/innovacion/apps/walletbot/settings_production.py']
capture_output = True
