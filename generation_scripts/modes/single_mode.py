from services import TopicService, SubtopicService, FlashcardService


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

            if output_type == 'TOPIC':
                content_service = TopicService()
            elif output_type == 'SUBTOPIC':
                content_service = SubtopicService()
            elif output_type == 'FLASHCARD':
                content_service = FlashcardService()

            content_service.generate_and_send(subject_type, number)
