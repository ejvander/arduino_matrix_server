from data_providers.DataProvider import DataProvider


class MessageProvider(DataProvider):
    def __init__(self):
        self.messages = [
            "%03%03%03%03Devan %26 Eric%03%03%03%03",
            "I Love You",
            "%0FDevan%0F",
        ]
        self.idx = 0

    def getMessage(self) -> str:
        message = self.messages[self.idx]
        self.idx = (self.idx + 1) % len(self.messages)
        return message