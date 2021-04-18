from data_providers.DataProvider import DataProvider


class MessageProvider(DataProvider):
    def __init__(self):
        self.messages = [
            "test",
        ]
        self.idx = 0

    def getMessage(self) -> str:
        message = self.messages[self.idx]
        self.idx = (self.idx + 1) % len(self.messages)
        return message