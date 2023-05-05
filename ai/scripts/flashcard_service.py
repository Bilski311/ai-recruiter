from content_saver import ContentSaver
from generators import FlashcardGenerator


class FlashcardService():
    def __init__(self):
        self.content_saver = ContentSaver()
        self.generator = FlashcardGenerator()

    def generate_and_send(self, subtopic_name, amount, ask_before_saving=True, topic_name=None):
        output = self.generator.generate(subtopic_name, amount, topic_name=topic_name)
        print(output)

        if output:
            self.content_saver.send_to_backend(
                self.generator, output, ask_before_saving)
