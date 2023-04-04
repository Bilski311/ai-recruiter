import requests
from requests.exceptions import HTTPError
from .base_client import BaseClient


class TopicClient(BaseClient):
    def __init__(self):
        super().__init__(endpoint="topic")

    def get_by_name(self, name):
        url = f"{self.url}/name/{name}"
        try:
            response = requests.get(url)
            response.raise_for_status()
        except HTTPError as e:
            e.response = response
            raise e

        return response.json()

    def saveAll(self, topics):
        for topic in topics:
            return requests.post(self.url, json=topic)

    def save(self, topic):
        return requests.post(self.url, json=topic)
