# walletbot
Telegram expense tracking bot

## Develop

**Setup**

```
$ git clone https://github.com/ogastorga/walletbot.git && cd walletbot
$ virtualenv -p /usr/bin/python3 .env
$ echo "export FLASK_APP=walletbot" >> .env/bin/activate
$ echo "export FLASK_DEBUG=1" >> .env/bin/activate
$ source .env/bin/activate
$ pip install -r requirements.txt
$ flask run
```
