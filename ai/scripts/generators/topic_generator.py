import json

class TopicGenerator:
    def __init__(self, content_generator):
        self.content_generator = content_generator
        self.output_type = 'TOPIC'

    def generateTopicsForJob(self, job_title, amount):
        return self.content_generator.generate(self.output_type, job_title=job_title, amount=amount)
