from .flashcard import flashcard_schema

subtopic_schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'flashcards': {
            'type': 'array',
            'items': flashcard_schema,
        },
        'topic_id': {'type': 'string'},
    },
    'additionalProperties': False,
    'required': ['name', 'topic_id'],
}
