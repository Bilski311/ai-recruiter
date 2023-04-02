from flask import Flask, jsonify, request
from pymongo import MongoClient
from jsonschema import validate, ValidationError
from documents.topic import topic_schema
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


@app.route('/topics', methods=['POST'])
def create_topic():
    try:
        validate(request.json, topic_schema)
    except ValidationError as e:
        return jsonify({'error': e.message}), 400
    else:
        topic_data = request.json
        topics.insert_one(topic_data)
        return jsonify({'message': 'Topic created successfully'}), 201


if __name__ == '__main__':
    app.run(debug=True)
