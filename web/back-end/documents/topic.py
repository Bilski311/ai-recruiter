from .subtopic import subtopic_schema
topic_schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string', },
        'subtopics': subtopic_schema,
    },
    'required': ['name'],
    'additionalProperties': False,
}