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
            Example:['btcusd', 'ethbtc', 'ethusd']
        """

        data = requests.get(self.url + "/symbols")
        pairs = data.json()

        return pairs

    def get_pair_details(self, pair: str) -> Dict[str, Any]:
        """
        Retrieves the details for the trading pair:

        Args:
            pair: Trading pair e.g."BTCGBP"
        Returns:
            Dictionary containing the details of the trading pair
            Example:{
                "symbol":"BTCUSD",
                "base_currency":"BTC",
                "quote_currency":"USD",
                "tick_size":1e-08,
                "quote_increment":0.01,
                "min_order_size":"0.00001",
                "status":"open",
                "wrap_enabled":false
            }
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
            Example:{
                    'bid': '6398.99',
                    'ask': '6399.00',
                    'volume': {
                                'BTC': '15122.8052525982',
                                'USD': '100216283.474911855175',
                                'timestamp': 1510407900000
                            },
                    'last': '6398.99'
                }
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
            Example:{
                    "symbol": "BTCUSD",
                    "open": "9121.76",
                    "high": "9440.66",
                    "low": "9106.51",
                    "close": "9347.66",
                    "changes": [
                        "9365.1",
                        "9386.16",
                        "9373.41",
                        "9322.56",
                        "9268.89",
                        "9265.38",
                        "9245",
                        "9231.43",
                        "9235.88",
                        "9265.8",
                        "9295.18",
                        "9295.47",
                        "9310.82",
                        "9335.38",
                        "9344.03",
                        "9261.09",
                        "9265.18",
                        "9282.65",
                        "9260.01",
                        "9225",
                        "9159.5",
                        "9150.81",
                        "9118.6",
                        "9148.01"
                    ],
                    "bid": "9345.70",
                    "ask": "9347.67"
                }
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
            Example:[
                        [
                        1559755800000,
                        7781.6,
                        7820.23,
                        7776.56,
                        7819.39,
                        34.7624802159
                        ],
                        [1559755800000,
                        7781.6,
                        7829.46,
                        7776.56,
                        7817.28,
                        43.4228281059],
                        ...
                    ]
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
            Dictionary with keys "bids" and "asks" and values
            as lists of dictionaries containing order book details as
            strings
            Example:{
                'bids': [
                {
                    "price": "3607.85",
                    "amount": "6.643373",
                    "timestamp": "1547147541"
                }
                ...
                ],
                'asks': [
                {
                    'price': '6400.00',
                    'amount': '3.04177064',
                    'timestamp': '1510408074'
                },
                ...
              ]
            }

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
            information for the pair
            Example:[
              {
                'timestamp': 1510408136,
                'timestampms': 1510408136595,
                'tid': 2199657585,
                'price': '6399.02',
                'amount': '0.03906848',
                'exchange': 'gemini',
                'type': 'buy'
              },
              ...
            ]
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
            Example:{
                        "closed_until_ms": 1474567602895,
                        "last_auction_price": "629.92",
                        "last_auction_quantity": "430.12917506",
                        "last_highest_bid_price": "630.10",
                        "last_lowest_ask_price": "632.44",
                        "last_collar_price": "631.27",
                        "next_auction_ms": 1474567782895
                    }
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
            List of dictionary objects containing the trade history
            information for the pair
            Example:[
                {
                    'last_auction_price': '6580.01',
                    'last_auction_quantity': '0.01515964',
                    'last_highest_bid_price': '6580.00',
                    'last_lowest_ask_price': '6580.01',
                    'next_update_ms': 1510433400000,
                    'next_auction_ms': 1510434000000,
                    'last_auction_eid': 2199289141
                },
                ...
            ]
        """

        if not since:
            data = requests.get(self.url + "/auction/" + pair)
        else:
            self.timestamp = date_to_unix_ts(since)
            data = requests.get(
                self.url + "/auction/{}?since={}".format(pair, self.timestamp)
            )

        auction_history = data.json()
        return auction_history

    def get_price_feed(self) -> List[Dict[str, str]]:
        """
        Retrieves list of dictionary containing price and percentage
        change in last 24h for each trading pair

        Returns:
            List of dictionaries containing the price and change in price
            for each pair
            Example:[
                        {
                            "pair":"BTCUSD",
                            "price":"9500.00",
                            "percentChange24h": "5.23"
                        },
                        {
                            "pair":"ETHUSD",
                            "price":"257.54",
                            "percentChange24h": "4.85"
                        },
                        {
                            "pair":"BCHUSD",
                            "price":"450.10",
                            "percentChange24h": "-2.91"
                        },
                        {
                            "pair":"LTCUSD",
                            "price":"79.50",
                            "percentChange24h": "7.63"
                        },
                        {
                            "pair":"ZECUSD",
                            "price":"72.89",
                            "percentChange24h": "-1.90"
                        }
                    ]
        """

        data = requests.get(self.url + "/pricefeed")
        price_feed = data.json()
        return price_feed
