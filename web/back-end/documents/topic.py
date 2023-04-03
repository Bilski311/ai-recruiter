from .subtopic import subtopic_schema

topic_schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string', },
        'subtopic_ids': {
            'type': 'array'
        },
    },
    'required': ['name'],
    'additionalProperties': False,
}
