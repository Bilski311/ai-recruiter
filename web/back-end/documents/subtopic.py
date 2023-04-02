subtopic_schema = {
    'type': 'array',
    'items': {
        'name': {'type': 'string'},
        'questions': {
            'type': 'array',
            'items': {
                'type': 'object',
                'properties': {
                    'question': {'type': 'string'},
                    'answer': {'type': 'string'},
                },
                'required': ['question', 'answer'],
                'additionalProperties': False,
            }
        },
        'required': ['name'],
    },
}
