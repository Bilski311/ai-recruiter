from content_generator import ContentGenerator
from content_saver import ContentSaver


class SingleMode:
    def __init__(self, user_input):
        self.user_input = user_input

    def run(self):
        while True:
            output_type = self.user_input.get_output_type()
            if output_type == 'Q':
                break

            subject_type = self.user_input.get_subject_type()
            number = self.user_input.get_number_of_outputs()

            content_generator = ContentGenerator(
                output_type, subject_type, number)
            content_generator.generate_and_send()
