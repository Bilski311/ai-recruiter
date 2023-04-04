import requests
from .base_client import BaseClient


class SubtopicClient(BaseClient):
    def __init__(self):
        super().__init__(endpoint="subtopic")

    def save_all(self, subtopics):
        for subtopic in subtopics:
            print(self.url)
            print(subtopic)
            requests.post(self.url, json=subtopic)

    def save(self, subtopic):
        requests.post(self.url, json=subtopic)
