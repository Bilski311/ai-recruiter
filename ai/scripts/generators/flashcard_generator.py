from requests.exceptions import HTTPError

from .output_types import FlashcardOutputType
from .base_generator import BaseGenerator
from .clients import TopicClient, SubtopicClient


class FlashcardGenerator(BaseGenerator):
    def __init__(self):
        super().__init__(FlashcardOutputType())
        self.topic_client = TopicClient()
        self.subtopic_client = SubtopicClient()

    def generate(self, subtopic_name, amount):
        subtopic = self.subtopic_client.get_by_name(subtopic_name)
        print(subtopic)
        flashcards = self.content_generator.generate(
            subtopic=subtopic['name'], amount=amount)

        existing_flashcards = subtopic.get('flashcards', [])
        subtopic['flashcards'] = existing_flashcards + flashcards

        return subtopic

    def save_all(self, subtopic):
        print(subtopic)
        self.subtopic_client.update(subtopic)

    def _get_or_create_subtopic(self, subtopic_name):
        try:
            return self.topic_client.get_by_name(subtopic_name)
        except HTTPError as e:
            if e.response.status_code == 404:
                response = self.topic_client.save({"name": topic_name})
                return response.json()['topicId']
            else:
                raise e
