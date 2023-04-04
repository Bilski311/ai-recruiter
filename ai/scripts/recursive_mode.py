from topic_service import TopicService
from subtopic_service import SubtopicService
from flashcard_service import FlashcardService


class RecursiveMode:
    def __init__(self, user_input):
        self.user_input = user_input

    def run(self):
        job_position = self.user_input.get_job_position()
        num_topics = self.user_input.get_number_of_topics()
        num_subtopics = self.user_input.get_number_of_subtopics()
        num_flashcards = self.user_input.get_number_of_flashcards()

        topic_service = TopicService()
        subtopic_service = SubtopicService()
        flashcard_service = FlashcardService()

        topic_service.generate_and_send(job_position, num_topics)
        topics = topic_service.get_all()
        print('TOPICS: ')
        print(topics)

        for topic in topics:
            print('GENERATING SUBTOPICS FOR TOPIC: ' + topic['name'])
            subtopic_service.generate_and_send(
                topic['name'], num_subtopics, ask_before_saving=False)
            subtopics = subtopic_service.get_all_for_topic(topic['name'])
            print(subtopics)

            for subtopic in subtopics:
                print('GENERATING FLASHCARDS FOR SUBTOPIC: ' +
                      subtopic['name'])
                flashcards = flashcard_service.generate_and_send(
                    subtopic['name'], num_flashcards, ask_before_saving=False)
