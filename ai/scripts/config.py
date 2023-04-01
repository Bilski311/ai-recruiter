CHAT_TEMPERATURE = 0
output_types = {
    'TOPIC': {
        'system_template': 'You are helping to generate a list of technical topics. They should group questions related to the recruitement process for the position of {subject}.',
        'human_template': 'Generate a list of 10 topics in JSON format. Write it out only in JSON format(no other text). The JSON should have the format [{{"topic": "Topic 1"}}, {{"topic": "Topic 2"}}].'
    },
    'SUBTOPIC': {
        'system_template': 'You are helping to generate a list of subtopics person applying for a job should know for the given topic: {subject}.',
        'human_template': 'Generate a list of 10 subtopics in JSON format. Write it out only in JSON format(no other text). The JSON should have the format [\n\t{{"subtopic": "Subtopic 1"}},\n\t {{"subtopic": "Subtopic 2"}}].'
    },
    'QUESTION': {
        'system_template': 'You are helping to generate dataset of questions for IT recruitement process related to {subject}.',
        'human_template': 'Generate a question. Write it out only in JSON format(no other text). The JSON should only have one field: "question"'
    }
}
