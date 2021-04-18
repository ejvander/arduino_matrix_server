from urllib3 import PoolManager
import json

from data_providers.DataProvider import DataProvider


class KanyeProvider(DataProvider):
    KANYE_REST_URL = "https://api.kanye.rest/"

    def __init__(self, http: PoolManager):
        self.http = http

    def getMessage(self) -> str:
        r = self.http.request("GET", self.KANYE_REST_URL)
        quote = json.loads(r.data.decode("utf-8"))

        return quote["quote"]