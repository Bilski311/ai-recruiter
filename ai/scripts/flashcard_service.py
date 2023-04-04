from content_service import ContentService
from generators import FlashcardGenerator


class FlashcardService(ContentService):
    def _get_generator(self):
        return FlashcardGenerator()
