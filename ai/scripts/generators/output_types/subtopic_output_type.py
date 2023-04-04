from .output_type import OutputType


class SubtopicOutputType(OutputType):
    def __init__(self):
        super().__init__(
            system_template='You are helping to generate a list of subtopics person applying for a job should know for the given topic: {topic}.',
            human_template='Generate a list of {amount} subtopics in JSON format. Write it out only in JSON format(no other text). The JSON should have the format [\n\t{{"name": "Subtopic 1"}},\n\t {{"name": "Subtopic 2"}}]. Do not use the character forward slash(/) in the subtopic names.',
            endpoint='subtopic'
        )
