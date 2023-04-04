from generators import TopicGenerator, SubtopicGenerator, FlashcardGenerator
from content_saver import ContentSaver


class ContentGenerator:
    def __init__(self, output_type, subject_type, number):
        self.output_type = output_type
        self.subject_type = subject_type
        self.number = number
        self.content_saver = ContentSaver()

    def get_generator(self):
        if self.output_type == 'TOPIC':
            return TopicGenerator()
        elif self.output_type == 'SUBTOPIC':
            return SubtopicGenerator()
        elif self.output_type == 'FLASHCARD':
            return FlashcardGenerator()
        else:
            return None

    def generate_and_send(self):
        generator = self.get_generator()
        output = None
        if generator:
            output = generator.generate(self.subject_type, self.number)
            print(output)
        else:
            print(f"Invalid output type: {self.output_type}")
            return None

        if output:
            self.content_saver.send_to_backend(generator, output)
