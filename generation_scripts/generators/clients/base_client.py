from config import BACKEND_URL


class BaseClient:
    def __init__(self, endpoint):
        self.url = BACKEND_URL + endpoint

    def saveAll(self, output):
        NotImplementedError

    def save(self, output):
        NotImplementedError
