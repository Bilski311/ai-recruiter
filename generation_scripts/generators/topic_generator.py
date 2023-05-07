from output_types import TopicOutputType
from .base_generator import BaseGenerator
from clients import TopicClient


class TopicGenerator(BaseGenerator):
    def __init__(self):
        super().__init__(TopicOutputType())
        self.topic_client = TopicClient()

    def generate(self, job_title, amount):
        return self.content_generator.generate(job_title=job_title, amount=amount)

    def save_all(self, topics):
        self.topic_client.save_all(topics)
