OPEN_AI_KEY = "OpenAIKey"


class PrivateAPIInfoTemplate:
    def __init__(self):
        self.keys = {}

    def getOpenAIKey(self):
        return self.keys[OPEN_AI_KEY];