from flask import Flask, jsonify
from pymongo import MongoClient
import os
import certifi

app = Flask(__name__)

client = MongoClient(os.environ['MONGO_URI'], tlsCAFile=certifi.where())
db = client['ai_recruiter']
topics = db['topics']


@app.route('/topics', methods=['GET'])
def get_topics():
    topics_list = []
    print(topics.find())
    for topic in topics.find():
        topic_dict = {'_id': str(topic['_id']), 'name': topic['name']}
        topics_list.append(topic_dict)
    return jsonify(topics_list)


if __name__ == '__main__':
    app.run(debug=True)
