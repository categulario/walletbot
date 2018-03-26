from walletbot import app
from pymongo import MongoClient


client = MongoClient(app.config['MONGO_URI']).walletbot
