CHAT_TEMPERATURE = 0
output_types = {
    'TOPIC': {
        'system_template': '',
        'human_template': ''
    },
    'SUBTOPIC': {
        'system_template': 'You are helping to generate a list of subtopics one should know for the given topic: {subject}.',
        'human_template': 'Generate a list of 50 subtopics in JSON format. Write it out only in JSON format(no other text). The JSON should have the format [{{"subtopic": "Subtopic 1"}}, {{"subtopic": "Subtopic 2"}}].'
    },
    'QUESTION': {
        'system_template': 'You are helping to generate dataset of questions for IT recruitement process related to {subject}.',
        'human_template': 'Generate a question. Write it out only in JSON format(no other text). The JSON should only have one field: "question"'
    }
}
