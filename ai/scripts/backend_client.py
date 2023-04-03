import ssl
import requests
from pymongo import MongoClient
from config import MONGO_URI, MONGO_DB, BACKEND_URL
import certifi


client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
db = client.test

db = client[MONGO_DB]


def save_topics(topics):
    for topic in topics:
        response = requests.post(BACKEND_URL, json=topic)
