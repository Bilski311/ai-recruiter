from content_service import ContentService
from generators import SubtopicGenerator, SubtopicClient


class SubtopicService(ContentService):
    def __init__(self):
        super().__init__()
        self.subtopic_client = SubtopicClient()

    def _get_generator(self):
        return SubtopicGenerator()

    def get_all_for_topic(self, topic_name):
        return self.subtopic_client.get_all_for_topic(topic_name)
