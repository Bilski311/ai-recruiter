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


@app.route('/topic/name/<string:topic_name>', methods=['GET'])
def get_topic_by_name(topic_name):
    topic = topics.find_one({'name': topic_name})
    if topic:
        topic['_id'] = str(topic['_id'])
        return jsonify(topic)
    else:
        return jsonify({'error': f'Topic with name {topic_name} does not exist'}), 404


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


@app.route('/subtopic/name/<string:subtopic_name>', methods=['GET'])
def get_subtopic_by_name(subtopic_name):
    subtopic = subtopics.find_one({'name': subtopic_name})
    if subtopic:
        subtopic['_id'] = str(subtopic['_id'])
        return jsonify(subtopic)
    else:
        return jsonify({'error': f'Topic with name {subtopic_name} does not exist'}), 404


@app.route('/subtopic', methods=['GET'])
def get_subtopics():
    subtopics_list = []
    print(subtopics.find())
    for subtopic in subtopics.find():
        subtopic['_id'] = str(subtopic['_id'])
        subtopics_list.append(subtopic)
    return jsonify(subtopics_list)


@app.route('/subtopic/topic_name/<string:topic_name>', methods=['GET'])
def get_subtopics_by_topic_name(topic_name):
    topic = topics.find_one({'name': topic_name})
    if not topic:
        return jsonify({'error': f'Topic with name {topic_name} does not exist'}), 404

    topic_id = topic['_id']
    print(topic_id)
    subtopics_list = []
    for subtopic in subtopics.find({'topic_id': topic_id}):
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
        topics.update_one({'_id': ObjectId(topic_id)}, {
                          '$push': {'subtopic_ids': subtopic_id}})
        return jsonify({'message': 'Subtopic created successfully', 'subtopicId': subtopic_id}), 201


@app.route('/subtopic/<string:subtopic_id>', methods=['PUT'])
def update_subtopic(subtopic_id):
    try:
        validate(request.json, subtopic_schema)
    except ValidationError as e:
        print(e)
        return jsonify({'error': e.message}), 400
    else:
        if subtopics.count_documents({'_id': ObjectId(subtopic_id)}) == 0:
            return jsonify({'error': f'Subtopic with ID {subtopic_id} does not exist'}), 400

        subtopic_data = request.json
        subtopics.update_one({'_id': ObjectId(subtopic_id)}, {
                             '$set': subtopic_data})
        return jsonify({'message': 'Subtopic updated successfully'})


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
