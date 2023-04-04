from .output_type import OutputType


class FlashcardOutputType(OutputType):
    def __init__(self):
        super().__init__(
            system_template='You are helping to generate dataset of questions for IT recruitement process related to {subtopic}.',
            human_template='Generate a list of {amount} questions. Write it out only in JSON format(no other text). The JSON should have the format [\n\t{{"question": "Question 1", "answer": "Answer 1"}},\n\t {{"question": "Question 2", "answer": "Answer 2"}}].'
        )
