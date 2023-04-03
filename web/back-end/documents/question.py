question_schema = {
    'type': 'object',
    'properties': {
        'question': {'type': 'string'},
        'answer': {'type': 'string'},
    },
    'required': ['question', 'answer'],
    'additionalProperties': False,
}
