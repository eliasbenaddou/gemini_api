from typing import Any, Dict, List

import requests

from gemini_api.utils import date_to_unix_ts


class Public:
    """
    Class to fetch public data from the Gemini REST API
    """

    def __init__(self, sandbox: bool = False) -> None:
        if sandbox:
            self.url = "https://api.sandbox.gemini.com/v1"
        else:
            self.url = "https://api.gemini.com/v1"

    def get_pairs(self) -> List[str]:
        """
        Retrieves an array of available trading pairs

        Returns:
            List of trading pairs, e.g. "BTCGBP"
        """

        data = requests.get(self.url + "/symbols")
        pairs = data.json()

        return pairs

    def get_pair_details(self, pair: str) -> Dict[str, Any]:
        """
        Retrieves the details for the trading pair

        Args:
            pair: Trading pair e.g."BTCGBP"
        Returns:
            Dictionary containing the details of the trading pair
        """
        data = requests.get(self.url + "/symbols/details/" + pair)
        details = data.json()
        return details

    def get_ticker(self, pair: str) -> Dict[str, Any]:
        """
        Retrieves information about recent trading activity for the
        trading pair, including bid size, last price and volume

        Args:
            pair: Trading pair e.g."BTCGBP"

        Returns:
            Dictionary containing the details of the pair's recent trades
        """

        data = requests.get(self.url + "/pubticker/" + pair)
        ticker = data.json()
        return ticker

    def get_ticker_prices(self, pair: str) -> Dict[str, Any]:
        """
        Retrieves information about recent trading activity for the
        trading pair, including open, close, high, low and prices
        from every hour.

        Args:
            pair: Trading pair e.g."BTCGBP"

        Returns:
            Dictionary containing the details of the pair's recent trades
        """
        v2_url = self.url.replace("v1", "v2")
        data = requests.get(v2_url + "/ticker/" + pair)
        ticker = data.json()
        return ticker

    def get_candles(self, pair: str, time_frame: str) -> List[List[float]]:
        """
        Retrieves time-intervaled data for the trading pair and time
        frame - accepts the following time frames: 1m, 5m, 15m, 30m,
        1hr, 6hr, 1day

        Args:
            pair: Trading pair e.g."BTCGBP"
            time_frame: Timeframe

        Returns:
            Nested lists of time-intervaled prices
        """
        v2_url = self.url.replace("v1", "v2")
        data = requests.get(v2_url + "/candles/" + pair + "/" + time_frame)
        candles = data.json()
        return candles

    def get_order_book(self, pair: str) -> Dict[str, List[Dict[str, str]]]:
        """
        Retrieves the current order book information, including bids
        and asks prices.

        The quantities and prices returned are returned as strings
        rather than numbers. The numbers returned are exact, not rounded,
        and it can be dangerous to treat them as floating point numbers.

        Args:
            pair: Trading pair e.g."BTCGBP"

        Returns:
            Dictionary with keys "bids" and "asks"
        """
        data = requests.get(self.url + "/book/" + pair)
        current_order_book = data.json()
        return current_order_book

    def get_trades_history(
        self, pair: str, since: str = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieves executed trades data since the specified timestamp as
        a whole number in unix time format, up to seven calendar days of
        market data. Returns most recent data if timestamp is not specified

        Args:
            pair: Trading pair e.g."BTCGBP"
            since: Date in YYYYDDMM format

        Returns:
            List of dictionary objects containing the trade history
        """

        if not since:
            data = requests.get(self.url + "/trades/" + pair)
        else:
            self.timestamp = date_to_unix_ts(since)
            data = requests.get(
                self.url + "/trades/{}?since={}".format(pair, self.timestamp)
            )

        trades_history = data.json()
        return trades_history

    def get_current_auction(self, pair: str) -> Dict[str, Any]:
        """
        Retrieves current auction information, including auction price
        or indicative price

        Args:
            pair: Trading pair e.g."BTCGBP"

        Returns:
            Dictionary of current auction information
        """
        data = requests.get(self.url + "/auction/" + pair)
        current_auction = data.json()
        return current_auction

    def get_auction_history(
        self, pair: str, since: str = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieves auction events data since the specified timestamp
        as a whole number in unix time format, up to seven calendar days
        of market data. Returns most recent data if timestamp is not
        specified.

        Args:
            pair: Trading pair e.g."BTCGBP"
            since: Date in YYYYDDMM format

        Returns:
            List of dictionary objects
        """

        if not since:
            data = requests.get(self.url + "/auction/" + pair + "/history")
        else:
            self.timestamp = date_to_unix_ts(since)
            data = requests.get(
                self.url
                + "/auction/history/{}?since={}".format(pair, self.timestamp)
            )

        auction_history = data.json()
        return auction_history

    def get_price_feed(self) -> List[Dict[str, str]]:
        """
        Retrieves list of dictionary containing price and percentage
        change in last 24h for each trading pair

        Returns:
            List of dictionaries containing the price and change in price
        """

        data = requests.get(self.url + "/pricefeed")
        price_feed = data.json()
        return price_feed
