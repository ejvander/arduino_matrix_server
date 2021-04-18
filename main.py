from typing import List

import urllib3
import urllib
import time

from data_providers.KanyeProvider import KanyeProvider
from data_providers.QuoteProvider import QuoteProvider
from data_providers.MessageProvider import MessageProvider
from data_providers.DataProvider import DataProvider
from data_providers.NewsProvider import NewsProvider
from config import SCREEN_URL

if __name__ == "__main__":

    idx = 0
    http = urllib3.PoolManager()

    data_providers: List[DataProvider] = [
        NewsProvider(http),
        KanyeProvider(http),
        QuoteProvider(http),
        MessageProvider(),
    ]

    while True:
        data_provider = data_providers[idx]
        message = data_provider.getMessage()

        idx = (idx + 1) % len(data_providers)

        http.request("GET", SCREEN_URL % (message,))

        message_len = len(urllib.parse.unquote(message))
        time.sleep(4 + (message_len * 4) / 10)
