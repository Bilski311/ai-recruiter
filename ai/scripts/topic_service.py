from content_service import ContentService
from generators import TopicGenerator, TopicClient


class TopicService(ContentService):
    def __init__(self):
        super().__init__()
        self.topic_client = TopicClient()

    def _get_generator(self):
        return TopicGenerator()

    def get_all(self):
        return self.topic_client.get_all()
