from __future__ import annotations

from typing import Any, Dict

from gemini_api.authentication import Authentication
from gemini_api.utils import date_to_unix_ts


class FXRate:
    """
    Class for FX Rate historical reference
    """

    __slots__ = [
        "_fx_pair",
        "_rate",
        "_as_of",
        "_provider",
        "_benchmark",
        "_result",
        "_message",
        "_reason",
    ]

    def __init__(
        self, auth: Authentication, fx_rate_data: Dict[str, Any]
    ) -> None:
        """
        Initialise FXRate class
        """
        if "fxPair" in fx_rate_data:
            self._fx_pair: str = fx_rate_data["fxPair"]
        if "rate" in fx_rate_data:
            self._rate: str = fx_rate_data["rate"]
        if "asOf" in fx_rate_data:
            self._as_of: int = fx_rate_data["asOf"]
        if "provider" in fx_rate_data:
            self._provider: str = fx_rate_data["provider"]
        if "benchmark" in fx_rate_data:
            self._benchmark: str = fx_rate_data["benchmark"]
        if "result" in fx_rate_data:
            self._result: str = fx_rate_data["result"]
        if "reason" in fx_rate_data:
            self._reason: str = fx_rate_data["reason"]
        if "message" in fx_rate_data:
            self._message: str = fx_rate_data["message"]

    @property
    def fx_pair(self) -> str:
        """
        Property for the requested currency pair

        Returns:
            Currency pair
        """
        return self._fx_pair

    @property
    def rate(self) -> str:
        """
        Property for the fx rate of the non USD currency. USD if the
        base currency and will always have a value of 1

        Returns:
            Rate
        """
        return self._rate

    @property
    def as_of(self) -> int:
        """
        Property for the timestamp that the requested fx rate has been
        retrieved for

        Returns:
            Timstamp in Epoch time format
        """
        return self._as_of

    @property
    def provider(self) -> str:
        """
        Property for the market data provider

        Returns:
            Market data provider
        """
        return self._provider

    @property
    def benchmark(self) -> str:
        """
        Property for the market for which the retrieved price applies to

        Returns:
            Market
        """
        return self._benchmark

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
    def get_fx_rate(
        cls, auth: Authentication, symbol: str, since: str
    ) -> FXRate:
        """
        Method to get the fx rate

        Timestamp is rounded to the closest timestamp received for an
        update from BCB

        Args:
            auth: Gemini authentication object
            symbol: Trading pair
            since: Date in YYYYMMDD format

        Returns:
            FXRate object
        """
        date_unix = date_to_unix_ts(since)
        path = f"/v2/fxrate/{symbol}/{date_unix}"

        res = auth.make_request(endpoint=path)
        return FXRate(auth=auth, fx_rate_data=res)
