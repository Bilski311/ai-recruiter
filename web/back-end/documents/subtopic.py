from .question import question_schema

subtopic_schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'questions': {
            'type': 'array',
            'items': question_schema,
        },
    },
    'additionalProperties': False,
    'required': ['name'],
}
