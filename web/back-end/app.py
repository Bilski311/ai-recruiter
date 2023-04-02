from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

client = MongoClient(os.environ['MONGO_URI'])
db = client['mydatabase']
topics = db['topics']


@app.route('/topics', methods=['GET'])
def get_topics():
    topics_list = []
    for topic in topics.find():
        topics_list.append(topic)
    return jsonify(topics_list)


if __name__ == '__main__':
    app.run(debug=True)
