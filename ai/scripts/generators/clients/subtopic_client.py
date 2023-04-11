import requests
from requests.exceptions import HTTPError
from urllib.parse import quote
from .base_client import BaseClient


class SubtopicClient(BaseClient):
    def __init__(self):
        super().__init__(endpoint="subtopic")

    def get_by_name(self, subtopic_name):
        url = f"{self.url}/name/{quote(subtopic_name)}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise e

    def save_all(self, subtopics):
        for subtopic in subtopics:
            requests.post(self.url, json=subtopic)

    def save(self, subtopic):
        subtopic['name'] = subtopic.get('name', None).replace('/', '%2F')
        requests.post(self.url, json=subtopic)

    def update(self, subtopic):
        subtopic_id = subtopic.get("_id", None)
        subtopic = self._remove_id_from_subtopic(subtopic)
        requests.put(self.url + f'/{subtopic_id}', json=subtopic)

    def get_all_for_topic(self, topic_name):
        url = f"{self.url}/topic_name/{topic_name}"
        try:
            response = requests.get(url)
            response.raise_for_status()
        except HTTPError as e:
            e.response = response
            raise e

        return response.json()

    def _remove_id_from_subtopic(self, subtopic):
        return {key: value for key, value in subtopic.items() if key != "_id"}
