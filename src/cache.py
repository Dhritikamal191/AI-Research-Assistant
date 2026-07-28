from functools import lru_cache

class ResponseCache:
    def __init__(self):
        self.cache = {}

    def get(self, question):
        return self.cache.get(question)

    def set(self, question, answer):
        self.cache[question] = answer

    def clear(self):
        self.cache.clear()

response_cache = ResponseCache()