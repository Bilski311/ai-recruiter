from .chat_output_generator import ChatOutputGenerator


class BaseGenerator:
    def __init__(self, output_type):
        self.output_type = output_type
        self.content_generator = ChatOutputGenerator(output_type)

    def generate(self, *args, **kwargs):
        raise NotImplementedError

    def save(self, output):
        raise NotImplementedError

    def save_all(self, output):
        raise NotImplementedError
