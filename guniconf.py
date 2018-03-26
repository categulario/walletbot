pidfile        = '/run/gunicorn/walletbot.pid'
bind           = ['0.0.0.0:5000']
user           = 'root'
group          = 'root'
accesslog      = '/var/log/gunicorn/walletbot.access.log'
errorlog       = '/var/log/gunicorn/walletbot.error.log'
raw_env        = ['WALLETBOT_SETTINGS=/root/apps/walletbot/settings_production.py']
capture_output = True
