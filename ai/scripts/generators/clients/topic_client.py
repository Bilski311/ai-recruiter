import requests
from .base_client import BaseClient


class TopicClient(BaseClient):
    def __init__(self):
        super().__init__(endpoint="topic")

    def get_by_name(self, name):
        url = self.url + '/name/' + name
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def saveAll(self, topics):
        for topic in topics:
            requests.post(self.url, json=topic)

    def save(self, topic):
        requests.post(self.url, json=topic)

    def getByName(self, name):
        response = requests.get(self.url, params={"name": name})
        return response.json()
