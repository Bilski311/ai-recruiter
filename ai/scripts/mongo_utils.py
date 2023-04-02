import ssl
from pymongo import MongoClient
from config import MONGO_URI, MONGO_DB
import certifi


client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
db = client.test

db = client[MONGO_DB]


def save_to_mongo(result, collection):
    collection = db[collection]
    collection.insert_many(result)
    client.close()
