from .output_types import QuestionOutputType
from .base_generator import BaseGenerator


class QuestionGenerator(BaseGenerator):
    def __init__(self):
        super().__init__(QuestionOutputType())

    def generateQuestionsForSubtopic(self, subtopic, amount):
        return self.generate_content(subtopic=subtopic, amount=amount)
