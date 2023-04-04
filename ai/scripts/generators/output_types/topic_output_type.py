from .output_type import OutputType

class TopicOutputType(OutputType):
    def __init__(self):
        super().__init__(
            system_template='You are helping to generate a list of technical topics. They should group questions related to the recruitement process for the position of {job_title}.',
            human_template='Generate a list of {amount} topics in JSON format. Write it out only in JSON format(no other text). The JSON should have the format [{{"name": "Topic 1"}}, {{"name": "Topic 2"}}]. Exclude any characters that are not part of the JSON(even the ones you use to properly display it in chat window)',
            endpoint='topic'
        )