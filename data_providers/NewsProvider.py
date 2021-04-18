from urllib3 import PoolManager
import json

from data_providers.DataProvider import DataProvider
from config import NEWSAPI_KEY


class NewsProvider(DataProvider):

    NEWS_URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWSAPI_KEY}"

    def __init__(self, http: PoolManager):
        self.http = http
        self.articles = []
        self.idx = 0

    def getMessage(self) -> str:
        if len(self.articles) == self.idx:
            self.idx = 0
            self.getHeadlines()

        message = self.createMessage()
        self.idx += 1
        return message

    def createMessage(self) -> str:
        article = self.articles[self.idx]

        return f"{article['title']}"

    def getHeadlines(self):
        r = self.http.request("GET", self.NEWS_URL)
        response_json = json.loads(r.data.decode("utf-8"))

        self.articles = response_json["articles"]
