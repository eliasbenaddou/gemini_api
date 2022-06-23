from __future__ import annotations

from typing import Any, Dict, List, Optional

from gemini_api.authentication import Authentication


class FeeVolume:
    """
    Class that manages Fee and Volumes APIs
    """

    __slots__ = [
        "_date",
        "_last_updated_ms",
        "_web_maker_fee_bps",
        "_web_taker_fee_bps",
        "_web_auction_fee_bps",
        "_api_maker_fee_bps",
        "_api_taker_fee_bps",
        "_api_auction_fee_bps",
        "_fix_maker_fee_bps",
        "_fix_taker_fee_bps",
        "_fix_auction_fee_bps",
        "_block_maker_fee_bps",
        "_block_taker_fee_bps",
        "_notional_30d_volume",
        "_notional_1d_volume",
        "_notional_1d_volume_date",
        "_notional_1d_volume_notional_volume",
        "_symbol",
        "_base_currency",
        "_notional_currency",
        "_data_date",
        "_total_volume_base",
        "_maker_buy_sell_ratio",
        "_buy_maker_base",
        "_buy_maker_notional",
        "_buy_maker_count",
        "_sell_maker_base",
        "_sell_maker_notional",
        "_sell_maker_count",
        "_buy_taker_base",
        "_buy_taker_notional",
        "_buy_taker_count",
        "_sell_taker_base",
        "_sell_taker_notional",
        "_sell_taker_count",
        "_result",
        "_reason",
        "_message",
    ]

    def __init__(
        self, auth: Authentication, volume_data: Dict[str, Any]
    ) -> None:
        """
        Initialise FeeVolume class
        """
        if "date" in volume_data:
            self._date: str = volume_data["date"]
        if "last_updated_ms" in volume_data:
            self._last_updated_ms: int = volume_data["last_updated_ms"]
        if "web_maker_fee_bps" in volume_data:
            self._web_maker_fee_bps: int = volume_data["web_maker_fee_bps"]
        if "web_taker_fee_bps" in volume_data:
            self._web_taker_fee_bps: int = volume_data["web_taker_fee_bps"]
        if "web_auction_fee_bps" in volume_data:
            self._web_auction_fee_bps: int = volume_data["web_auction_fee_bps"]
        if "api_maker_fee_bps" in volume_data:
            self._api_maker_fee_bps: int = volume_data["api_maker_fee_bps"]
        if "api_taker_fee_bps" in volume_data:
            self._api_taker_fee_bps: int = volume_data["api_taker_fee_bps"]
        if "api_auction_fee_bps" in volume_data:
            self._api_auction_fee_bps: int = volume_data["api_auction_fee_bps"]
        if "fix_maker_fee_bps" in volume_data:
            self._fix_maker_fee_bps: int = volume_data["fix_maker_fee_bps"]
        if "fix_taker_fee_bps" in volume_data:
            self._fix_taker_fee_bps: int = volume_data["fix_taker_fee_bps"]
        if "fix_auction_fee_bps" in volume_data:
            self._fix_auction_fee_bps: int = volume_data["fix_auction_fee_bps"]
        if "block_maker_fee_bps" in volume_data:
            self._block_maker_fee_bps: int = volume_data["block_maker_fee_bps"]
        if "block_taker_fee_bps" in volume_data:
            self._block_taker_fee_bps: int = volume_data["block_taker_fee_bps"]
        if "notional_30d_volume" in volume_data:
            self._notional_30d_volume: int = volume_data["notional_30d_volume"]
        if "notional_1d_volume" in volume_data:
            self._notional_1d_volume: List[Dict[str, Any]] = volume_data[
                "notional_1d_volume"
            ]
        if "symbol" in volume_data:
            self._symbol: str = volume_data["symbol"]
        if "base_currency" in volume_data:
            self._base_currency: float = volume_data["base_currency"]
        if "notional_currency" in volume_data:
            self._notional_currency: float = volume_data["notional_currency"]
        if "data_date" in volume_data:
            self._data_date: str = volume_data["data_date"]
        if "total_volume_base" in volume_data:
            self._total_volume_base: float = volume_data["total_volume_base"]
        if "maker_buy_sell_ratio" in volume_data:
            self._maker_buy_sell_ratio: float = volume_data[
                "maker_buy_sell_ratio"
            ]
        if "buy_maker_base" in volume_data:
            self._buy_maker_base: float = volume_data["buy_maker_base"]
        if "buy_maker_notional" in volume_data:
            self._buy_maker_notional: float = volume_data["buy_maker_notional"]
        if "buy_maker_count" in volume_data:
            self._buy_maker_count: float = volume_data["buy_maker_count"]
        if "sell_maker_base" in volume_data:
            self._sell_maker_base: float = volume_data["sell_maker_base"]
        if "sell_maker_notional" in volume_data:
            self._sell_maker_notional: float = volume_data[
                "sell_maker_notional"
            ]
        if "sell_maker_count" in volume_data:
            self._sell_maker_count: float = volume_data["sell_maker_count"]
        if "buy_taker_base" in volume_data:
            self._buy_taker_base: float = volume_data["buy_taker_base"]
        if "buy_taker_notional" in volume_data:
            self._buy_taker_notional: float = volume_data["buy_taker_notional"]
        if "buy_taker_count" in volume_data:
            self._buy_taker_count: float = volume_data["buy_taker_count"]
        if "sell_taker_base" in volume_data:
            self._sell_taker_base: float = volume_data["sell_taker_base"]
        if "sell_taker_notional" in volume_data:
            self._sell_taker_notional: float = volume_data[
                "sell_taker_notional"
            ]
        if "sell_taker_count" in volume_data:
            self._sell_taker_count: float = volume_data["sell_taker_count"]
        if "result" in volume_data:
            self._result: str = volume_data["result"]
        if "reason" in volume_data:
            self._reason: str = volume_data["reason"]
        if "message" in volume_data:
            self._message: str = volume_data["message"]

    @property
    def date(self) -> str:
        """
        Property for the UTC date

        Returns:
            date in yyyy-mm-dd format
        """
        return self._date

    @property
    def last_updated_ms(self) -> int:
        """
        Property for the last update timestamp

        Returns:
            Unix timestamp in millisecond of the last update
        """
        return self._last_updated_ms

    @property
    def web_maker_fee_bps(self) -> int:
        """
        Property for the web maker fee

        Returns:
            Maker fee for all symbols in basis point for web orders
        """
        return self._web_maker_fee_bps

    @property
    def web_taker_fee_bps(self) -> int:
        """
        Property for the web taker fee

        Returns:
            Taker fee for all symbols in basis point for web orders
        """
        return self._web_taker_fee_bps

    @property
    def web_auction_fee_bps(self) -> int:
        """
        Property for the web auction fee

        Returns:
            Auction fee for all symbols in basis point for web orders
        """
        return self._web_auction_fee_bps

    @property
    def api_maker_fee_bps(self) -> int:
        """
        Property for the api maker fee

        Returns:
            Maker fee for all symbols in basis point for API orders
        """
        return self._api_maker_fee_bps

    @property
    def api_taker_fee_bps(self) -> int:
        """
        Property for the api taker fee
        Returns:
            Taker fee for all symbols in basis point for API orders
        """
        return self._api_taker_fee_bps

    @property
    def api_auction_fee_bps(self) -> int:
        """
        Property for the api auction fee

        Returns:
            Auction fee for all symbols in basis point for API orders
        """
        return self._api_auction_fee_bps

    @property
    def fix_maker_fee_bps(self) -> int:
        """
        Property for the fix maker fee

        Returns:
            Maker fee for all symbols in basis point for FIX orders
        """
        return self._fix_maker_fee_bps

    @property
    def fix_taker_fee_bps(self) -> int:
        """
        Property for the fix taken fee

        Returns:
            Taker fee for all symbols in basis point for FIX orders
        """
        return self._fix_taker_fee_bps

    @property
    def fix_auction_fee_bps(self) -> int:
        """
        Property for the fix auction fee

        Returns:
            Auction fee for all symbols in basis point for FIX orders
        """
        return self._fix_auction_fee_bps

    @property
    def block_maker_fee_bps(self) -> int:
        """
        Property for the block maker fee

        Returns:
            Maker fee for all symbols in basis point for block orders
        """
        return self._block_maker_fee_bps

    @property
    def block_taker_fee_bps(self) -> int:
        """
        Property for the block taker fee

        Returns:
            Taker fee for all symbols in basis point for block orders
        """
        return self._block_taker_fee_bps

    @property
    def notional_30d_volume(self) -> float:
        """
        Property for the notional 30 day trading volume for the past
        30 days, including auction volume

        Returns:
            Maker plus taker trading volume
        """
        return self._notional_30d_volume

    @property
    def notional_1d_volume(self) -> List[Dict[str, Any]]:
        """
        Property for the 1 day notional 1 day trading volume for the past
        30 days

        Returns:
            List of 1 day notional volumes
        """
        return self._notional_1d_volume

    @property
    def symbol(self) -> str:
        """
        Property for the symbol

        Returns:
            Symbol
        """
        return self._symbol

    @property
    def base_currency(self) -> float:
        """
        Property for the base currency that the quantity is denominated in

        Returns:
            Base currency
        """
        return self._base_currency

    @property
    def notional_currency(self) -> float:
        """
        Property for the notional currency - price is denominated as
        the amount of notional currency per one unit of base currency

        Returns:
            Notional currency
        """
        return self._notional_currency

    @property
    def data_date(self) -> str:
        """
        Property for the data date

        Returns:
            UTC date in yyyy-mm-dd format
        """
        return self._data_date

    @property
    def total_volume_base(self) -> float:
        """
        Property for the total volume base

        Returns:
            Total trade volume for this day
        """
        return self._total_volume_base

    @property
    def maker_buy_sell_ratio(self) -> float:
        """
        Property for the maker buy/sell ratio - the proportion of maker
        base volume on trades where the account was on the buy side
        versus all maker trades. If no maker base volume on the buy
        side, then this value is 0

        Returns:
            Maker buy/sell ratio
        """
        return self._maker_buy_sell_ratio

    @property
    def buy_maker_base(self) -> float:
        """
        Property for the buy maker base where the account was a maker
        on the buy side of the trade

        Returns:
            Quantity for this day
        """
        return self._buy_maker_base

    @property
    def buy_maker_notional(self) -> float:
        """
        Property for the notional value where the account was a maker
        on the buy side of the trade

        Returns:
            Notional value for this day
        """
        return self._buy_maker_notional

    @property
    def buy_maker_count(self) -> float:
        """
        Property for the buy maker count where the account was a maker
        on the buy side of the trade

        Returns:
            Number of trades for this day
        """
        return self._buy_maker_count

    @property
    def sell_maker_base(self) -> float:
        """
        Property for the sell maker base where the account was a maker
        on the sell side of the trade

        Returns:
            Quantity for this day
        """
        return self._sell_maker_base

    @property
    def sell_maker_notional(self) -> float:
        """
        Property for the sell maker notional value where the account
        was a maker on the sell side of the trade

        Returns:
            Notional value for this day
        """
        return self._sell_maker_notional

    @property
    def sell_maker_count(self) -> float:
        """
        Property for the sell maker count where the account was a maker
        on the sell side of the trade

        Returns:
            Number of trades for this day
        """
        return self._sell_maker_count

    @property
    def buy_taker_base(self) -> float:
        """
        Property for the buy taker base value where the account was a
        taker on the buy side of the trade

        Returns:
            Quantity for this day
        """
        return self._buy_taker_base

    @property
    def buy_taker_notional(self) -> float:
        """
        Property for the buy taker notional value where the account was
        a taker on the buy side of the trade

        Returns:
            Notional value for this day
        """
        return self._buy_taker_notional

    @property
    def buy_taker_count(self) -> float:
        """
        Property for the buy taker count where the account was a taker
        on the buy side of the trade

        Returns:
            Number of trades for this day
        """
        return self._buy_taker_count

    @property
    def sell_taker_base(self) -> float:
        """
        Property for the sell taker base where the account was a taker
        on the sell side of the trade

        Returns:
            Quantity for this day
        """
        return self._sell_taker_base

    @property
    def sell_taker_notional(self) -> float:
        """
        Property for the sell taker notional value where the account was
        a taker on the sell side of the trade

        Returns:
            Notional value for this day
        """
        return self._sell_taker_notional

    @property
    def sell_taker_count(self) -> float:
        """
        Property for the sell taker count where the account was a taker
        on the sell side of the trade

        Returns:
            Number of trades for this day
        """
        return self.sell_taker_count

    @property
    def result(self) -> str:
        """
        Property for the result upon errors or the state of a request

        Returns:
            Result
        """
        return self._result

    @property
    def reason(self) -> str:
        """
        Property for the reason of errors

        Returns:
            Short error description
        """
        return self._reason

    @property
    def message(self) -> str:
        """
        Property for the error message

        Returns:
            Error message description
        """
        return self._message

    @classmethod
    def get_notional_volume(cls, auth: Authentication) -> Optional[FeeVolume]:
        """
        Method to get the notional volume in price currency that has
        been traded across all pairs over a period of 30 days.

        Args:
            auth: Gemini authentication object

        Returns:
            FeeVolume object

        """
        path = "/v1/notionalvolume"

        res = auth.make_request(endpoint=path)
        return FeeVolume(auth=auth, volume_data=res)

    @classmethod
    def get_trade_volume(cls, auth: Authentication) -> List[FeeVolume]:
        """
        Method to
        Args:
            auth: Gemini authentication object

        Returns:
            FeeVolume object

        """
        path = "/v1/tradevolume"

        res = auth.make_request(endpoint=path)

        all_trade_volume = []

        for i in range(len(res[0])):
            trade_volume = FeeVolume(auth=auth, volume_data=res[0][i])
            all_trade_volume.append(trade_volume)

        return all_trade_volume
