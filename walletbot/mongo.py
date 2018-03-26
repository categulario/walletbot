from pymongo import MongoClient
from walletbot import app


client = MongoClient(app.config['MONGO_URI']).walletbot
