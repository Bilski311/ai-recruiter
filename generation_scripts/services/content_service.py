from content_saver import ContentSaver


from abc import ABC, abstractmethod


class ContentService(ABC):
    def __init__(self):
        self.content_saver = ContentSaver()

    @abstractmethod
    def _get_generator(self):
        pass

    def generate_and_send(self, subject_type, number, ask_before_saving=True):
        generator = self._get_generator()
        output = generator.generate(subject_type, number)
        print(output)

        if output:
            self.content_saver.send_to_backend(
                generator, output, ask_before_saving)
