from typing import List

from urllib3 import PoolManager
import json

from data_providers.DataProvider import DataProvider
from config import ALPHA_VANTAGE_API_KEY


class QuoteProvider(DataProvider):

    ALPHA_VANTAGE_STOCK_URL = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=%s&apikey={ALPHA_VANTAGE_API_KEY}"

    STOCKS = ["MSFT", "AAPL", "SPY", "QQQ", "SOXX"]

    def __init__(self, http: PoolManager):
        self.idx = 0
        self.http = http

    def getMessage(self) -> str:
        message = self.requestAlphaVantage(self.STOCKS[self.idx])
        self.idx = (self.idx + 1) % len(self.STOCKS)
        return message

    def process_quote(self, quote):
        try:
            quote_data = quote["Global Quote"]
            symbol = quote_data["01. symbol"]
            price = float(quote_data["05. price"])
            change = float(quote_data["09. change"])
            change_pct = round(float(quote_data["10. change percent"][0:-1]), 2)

            change_str = "%1E" + str(change) if change > 0 else "%1F" + str(abs(change))
            change_pct_str = (
                "%1E" + str(change_pct)
                if change_pct > 0
                else "%1F" + str(abs(change_pct))
            )

            return f"{symbol} {price} {change_str} {change_pct_str}%25"
        except:
            return ""

    def requestAlphaVantage(self, stock: str) -> str:
        stock_api_url = self.ALPHA_VANTAGE_STOCK_URL % (stock,)

        r = self.http.request("GET", stock_api_url)
        quote = json.loads(r.data.decode("utf-8"))

        return self.process_quote(quote)