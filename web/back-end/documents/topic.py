from .subtopic import subtopic_schema

topic_schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string', },
        'subtopics': {
            'type': 'array',
            'items': subtopic_schema,
        },
    },
    'required': ['name'],
    'additionalProperties': False,
}
