from .output_types import SubtopicOutputType
from .base_generator import BaseGenerator
from . clients import TopicClient, SubtopicClient


class SubtopicGenerator(BaseGenerator):
    def __init__(self):
        super().__init__(SubtopicOutputType())
        self.topic_client = TopicClient()
        self.subtopic_client = SubtopicClient()

    def generate(self, topic_name, amount):
        subtopics = self.content_generator.generate(
            topic=topic_name, amount=amount)
        topic = self.topic_client.get_by_name(topic_name)
        for subtopic in subtopics:
            subtopic["topic_id"] = topic["_id"]

        return subtopics

    def save_all(self, subtopics):
        self.subtopic_client.save_all(subtopics)
