from pymongo import MongoClient
from config import MONGO_URI, MONGO_DB, MONGO_COLLECTION

def save_to_mongo(result, collection):
    client = MongoClient(MONGO_URI)
    db = client[MONGO_DB]
    collection = db[collection]
    collection.insert_many(result)
    client.close()
