from requests.exceptions import HTTPError

from .output_types import SubtopicOutputType
from .base_generator import BaseGenerator
from .clients import TopicClient, SubtopicClient


class SubtopicGenerator(BaseGenerator):
    def __init__(self):
        super().__init__(SubtopicOutputType())
        self.topic_client = TopicClient()
        self.subtopic_client = SubtopicClient()

    def generate(self, topic_name, amount):
        subtopics = self.content_generator.generate(
            topic=topic_name, amount=amount)
        topic_id = self._get_or_create_topic_id(topic_name)
        for subtopic in subtopics:
            subtopic["topic_id"] = topic_id

        return subtopics

    def save_all(self, subtopics):
        self.subtopic_client.save_all(subtopics)

    def _get_or_create_topic_id(self, topic_name):
        try:
            response = self.topic_client.get_by_name(topic_name)['_id']
            return response
        except HTTPError as e:
            if e.response.status_code == 404:
                response = self.topic_client.save({"name": topic_name})
                return response.json()['topicId']
            else:
                raise e
