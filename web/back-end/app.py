from flask import Flask, jsonify, request
from pymongo import MongoClient
from jsonschema import validate, ValidationError
from documents.topic import topic_schema
from documents.subtopic import subtopic_schema
import os
import certifi
import json
from bson import ObjectId

app = Flask(__name__)

client = MongoClient(os.environ['MONGO_URI'], tlsCAFile=certifi.where())
db = client['ai_recruiter']
topics = db['topics']
subtopics = db['subtopics']


@app.route('/topic', methods=['GET'])
def get_topics():
    topics_list = []
    for topic in topics.find():
        topic['_id'] = str(topic['_id'])
        topics_list.append(topic)
    return jsonify(topics_list)


@app.route('/topic', methods=['POST'])
def create_topic():
    try:
        validate(request.json, topic_schema)
    except ValidationError as e:
        return jsonify({'error': e.message}), 400
    else:
        topic_id = save_topic(request.json) 
        return jsonify({'message': 'Topic created successfully', 'topicId': topic_id}), 201

@app.route('/subtopic', methods=['GET'])
def get_subtopics():
    subtopics_list = []
    print(subtopics.find())
    for subtopic in subtopics.find():
        subtopic['_id'] = str(subtopic['_id'])
        subtopics_list.append(subtopic)
    return jsonify(subtopics_list)

@app.route('/subtopic', methods=['POST'])
def create_subtopic():
    try:
        validate(request.json, subtopic_schema)
    except ValidationError as e:
        return jsonify({'error': e.message}), 400
    else:
        topic_id = request.json['topic_id']
        if topics.count_documents({'_id': ObjectId(topic_id)}) == 0:
            return jsonify({'error': f'Topic with ID {topic_id} does not exist'}), 400
        subtopic_id = save_subtopic(request.json)
        topics.update_one({'_id': ObjectId(topic_id)}, {'$push': {'subtopic_ids': subtopic_id}})
        return jsonify({'message': 'Subtopic created successfully', 'subtopicId': subtopic_id}), 201


def save_topic(topic):
    topic_data = request.json
    result = topics.insert_one(topic_data)
    return str(result.inserted_id)

def save_subtopic(subtopic):
    subtopic_data = request.json
    result = subtopics.insert_one(subtopic_data)
    return str(result.inserted_id)

if __name__ == '__main__':
    app.run(debug=True)
