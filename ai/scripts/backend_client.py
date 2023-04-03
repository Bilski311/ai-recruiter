import requests
from config import BACKEND_URL, output_types


def save_topics(topics):
    for topic in topics:
        response = requests.post(BACKEND_URL + output_types['TOPIC']['endpoint'], json=topic)

def save_subtopics(subtopics):
    for subtopic in subtopics:
        response = requests.post(BACKEND_URL + output_types['SUBTOPIC']['endpoint'], json=subtopic)
