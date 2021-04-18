from typing import List

import urllib3
import urllib
import json
import time

from data_providers.KanyeProvider import KanyeProvider
from data_providers.QuoteProvider import QuoteProvider
from data_providers.MessageProvider import MessageProvider
from data_providers.DataProvider import DataProvider
from config import SCREEN_URL

if __name__ == "__main__":

    idx = 0
    http = urllib3.PoolManager()

    data_providers: List[DataProvider] = [
        KanyeProvider(http),
        QuoteProvider(http),
        MessageProvider(),
    ]

    while True:
        data_provider = data_providers[idx]
        message = data_provider.getMessage()

        idx = (idx + 1) % len(data_providers)

        http.request("GET", SCREEN_URL % (message,))
        time.sleep(len(message) / 2)
