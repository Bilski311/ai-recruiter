import os 

CHAT_TEMPERATURE = 0
MONGO_URI = os.environ['MONGO_URI']
MONGO_DB = "ai_recruiter"
MONGO_COLLECTION = "generated_content"
SAVE_TO_MONGO = False
BACKEND_URL = "http://localhost:5000/"

output_types = {
    'TOPIC': {
        'system_template': 'You are helping to generate a list of technical topics. They should group questions related to the recruitement process for the position of {subject}.',
        'human_template': 'Generate a list of {number} topics in JSON format. Write it out only in JSON format(no other text). The JSON should have the format [{{"name": "Topic 1"}}, {{"name": "Topic 2"}}]. Exclude any characters that are not part of the JSON(even the ones you use to properly display it in chat window)',
        'endpoint': 'topic'
    },
    'SUBTOPIC': {
        'system_template': 'You are helping to generate a list of subtopics person applying for a job should know for the given topic: {subject}.',
        'human_template': 'Generate a list of {number} subtopics in JSON format. Write it out only in JSON format(no other text). The JSON should have the format [\n\t{{"subtopic": "Subtopic 1"}},\n\t {{"subtopic": "Subtopic 2"}}].',
        'endpoint': 'subtopic',
        
    },
    'QUESTION': {
        'system_template': 'You are helping to generate dataset of questions for IT recruitement process related to {subject}.',
        'human_template': 'Generate a list of {number} questions. Write it out only in JSON format(no other text). The JSON should only have one field: "question"'
    }
}
