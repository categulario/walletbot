from fabric.api import run, cd, env, sudo
from fabric.context_managers import prefix
from os import environ


SERVER_HOST = environ.get('SERVER_HOST')
SERVER_USER = environ.get('SERVER_USER')
SERVER_PASSWORD = environ.get('SERVER_HOST')
SERVER_PATH = environ.get('SERVER_PATH')

env.hosts    = [SERVER_HOST]
env.user     = SERVER_USER
env.password = SERVER_PASSWORD

def deploy():
    with cd(SERVER_PATH):
        run('git pull')

        with prefix('source .env/bin/activate'):
            run('pip install -r requirements.txt')
            sudo('systemctl restart walletbot')
