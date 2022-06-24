from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from gemini_api.authentication import Authentication
from gemini_api.utils import date_to_unix_ts


class Order:
    """
    Class that manages order book placement to create new orders,
    wrap orders and cancel orders.
    """

    __slots__ = [
        "_order_id",
        "_id",
        "_client_order_id",
        "_symbol",
        "_exchange",
        "_avg_execution_price",
        "_side",
        "_order_type",
        "_timestamp",
        "_timestampms",
        "_trades",
        "_is_live",
        "_is_cancelled",
        "_reason",
        "_is_hidden",
        "_was_forced",
        "_executed_amount",
        "_remaining_amount",
        "_options",
        "_price",
        "_amount",
        "_original_amount",
        "_remaining_amount",
        "_pair",
        "_price_currency",
        "_quantity",
        "_quantity_currency",
        "_total_spend",
        "_total_spend_currency",
        "_fee",
        "_fee_currency",
        "_fee_amount",
        "_deposit_fee",
        "_deposit_fee_currency",
        "_trade_id",
        "_aggressor",
        "_is_auction_fill",
        "_is_clearing_fill",
        "_break_type",
        "_reason",
        "_result",
        "_message",
    ]

    def __init__(
        self, auth: Authentication, order_data: Dict[Any, Any]
    ) -> None:
        """
        Initialise Order class
        """
        if "order_id" in order_data:
            if isinstance(order_data["order_id"], str):
                self._order_id: Union[str, Dict[int, bool]] = order_data[
                    "order_id"
                ]
            else:
                if isinstance(order_data["order_id"], dict):
                    self._order_id = list(order_data["order_id"].keys())[0]
                    self._is_cancelled: bool = list(
                        order_data["order_id"].values()
                    )[0]
        if "orderId" in order_data:
            self._order_id = order_data["orderId"]
        if "id" in order_data:
            self._id: str = order_data["id"]
        if "client_order_id" in order_data:
            self._client_order_id: str = order_data["client_order_id"]
        if "symbol" in order_data:
            self._symbol: str = order_data["symbol"]
        if "exchange" in order_data:
            self._exchange: str = order_data["exchange"]
        if "avg_execution_price" in order_data:
            self._avg_execution_price: str = order_data["avg_execution_price"]
        if "side" in order_data:
            self._side: str = order_data["side"]
        if "type" in order_data:
            self._order_type: str = order_data["type"]
        if "timestamp" in order_data:
            self._timestamp: str = order_data["timestamp"]
        if "timestampms" in order_data:
            self._timestampms: int = order_data["timestampms"]
        if "trades" in order_data:
            self._trades: List[Dict[str, Union[str, Any]]] = order_data[
                "trades"
            ]
        if "is_live" in order_data:
            self._is_live: bool = order_data["is_live"]
        if "is_cancelled" in order_data:
            self._is_cancelled = order_data["is_cancelled"]
        if "is_hidden" in order_data:
            self._is_hidden: bool = order_data["is_hidden"]
        if "was_forced" in order_data:
            self._was_forced: bool = order_data["was_forced"]
        if "executed_amount" in order_data:
            self._executed_amount: float = order_data["executed_amount"]
        if "remaining_amount" in order_data:
            self._remaining_amount: str = order_data["remaining_amount"]
        if "options" in order_data:
            self._options: List[str] = order_data["options"]
        if "price" in order_data:
            self._price: str = order_data["price"]
        if "original_amount" in order_data:
            self._original_amount: str = order_data["original_amount"]
        if "pair" in order_data:
            self._pair: str = order_data["pair"]
        if "priceCurrency" in order_data:
            self._price_currency: str = order_data["priceCurrency"]
        if "quantity" in order_data:
            self._quantity: str = order_data["quantity"]
        if "quantityCurrency" in order_data:
            self._quantity_currency: str = order_data["quantityCurrency"]
        if "totalSpend" in order_data:
            self._total_spend: str = order_data["totalSpend"]
        if "totalSpendCurrency" in order_data:
            self._total_spend_currency: str = order_data["totalSpendCurrency"]
        if "fee" in order_data:
            self._fee: str = order_data["fee"]
        if "feeCurrency" in order_data:
            self._fee_currency: str = order_data["feeCurrency"]
        if "fee_currency" in order_data:
            self._fee_currency = order_data["fee_currency"]
        if "depositFee" in order_data:
            self._deposit_fee: str = order_data["depositFee"]
        if "depositFeeCurrency" in order_data:
            self._deposit_fee_currency: str = order_data["depositFeeCurrency"]
        if "amount" in order_data:
            self._amount: float = order_data["amount"]
        if "aggressor" in order_data:
            self._aggressor: bool = order_data["aggressor"]
        if "fee_amount" in order_data:
            self._fee_amount: str = order_data["fee_amount"]
        if "tid" in order_data:
            self._trade_id: int = order_data["tid"]
        if "is_auction_fill" in order_data:
            self._is_auction_fill: bool = order_data["is_auction_fill"]
        if "is_clearing_fill" in order_data:
            self._is_clearing_fill: bool = order_data["is_clearing_fill"]
        if "break" in order_data:
            self._break_type: str = order_data["break"]
        if "result" in order_data:
            self._result: str = order_data["result"]
        if "reason" in order_data:
            self._reason: str = order_data["reason"]
        if "message" in order_data:
            self._message: str = order_data["message"]

    @property
    def order_id(self) -> Union[str, Dict[int, bool]]:
        """
        Property for the order ID

        Returns:
            Order ID
        """
        return self._order_id

    @property
    def id(self) -> str:
        """
        Property for the ID

        Returns:
            ID
        """
        return self._id

    @property
    def client_order_id(self) -> str:
        """
        Property for the Client Order ID

        Returns:
            Client Order ID
        """
        return self._client_order_id

    @property
    def symbol(self) -> str:
        """
        Property for the symbol of the order

        Returns:
            Symbol
        """
        return self._symbol

    @property
    def exchange(self) -> str:
        """
        Property for the exchange (always "gemini")

        Returns:
            exchange
        """
        return self._exchange

    @property
    def avg_execution_price(self) -> str:
        """
        Property for the average price at which this order as been
        executed so far. 0 if the order has not been executed at all

        Returns:
            avg_execution_price
        """
        return self._avg_execution_price

    @property
    def side(self) -> str:
        """
        Property for the side (either "buy" or "sell")

        Returns:
            Side
        """
        return self._side

    @property
    def order_type(self) -> str:
        """
        Property for the description of the type:
        exchange limit, auction-only exchange limit, market buy,
        market sell, indication-of-interest

        Returns:
            type
        """
        return self._order_type

    @property
    def timestamp(self) -> str:
        """
        Property for the  timestamp the order was submitted. Note that
        for compatibility reasons, this is returned as a string.
        Recommend using the timestampms field instead

        Returns:
            The number of seconds since 1970-01-01 UTC (unix epoch)
        """
        return self._timestamp

    @property
    def timestampms(self) -> int:
        """
        Property for the timestamp the order was submitted in milliseconds

        Returns:
            The number of milliseconds since 1970-01-01 UTC
        """
        return self._timestampms

    @property
    def trades(self) -> List[Dict[str, Any]]:
        """
        Property for the trades containing trade details

        Returns:
            List of trade dictionary objects
        """
        return self._trades

    @property
    def is_live(self) -> bool:
        """
        Property for the active status of an order

        Returns:
            True if the order is on the book (has remaining quantity
            and has not been canceled), false otherwise
        """
        return self._is_live

    @property
    def is_cancelled(self) -> bool:
        """
        Property for the cancelled status of an order

        Returns:
            True if the order has been canceled
        """
        return self._is_cancelled

    @property
    def is_hidden(self) -> bool:
        """
        Property for the hidden status of an order

        Returns:
            Will always return false unless the order was placed with
            the indication-of-interest execution option.
        """
        return self._is_hidden

    @property
    def was_forced(self) -> bool:
        """
        Property for the forced status of an order (always False)

        Returns:
            False.
        """
        return self._was_forced

    @property
    def executed_amount(self) -> float:
        """
        Property for the amount of the order that has been filled

        Returns:
            Executed amount
        """
        return self._executed_amount

    @property
    def remaining_amount(self) -> str:
        """
        Property for the amount of the order that has not been filled

        Returns:
            Remaining amount
        """
        return self._remaining_amount

    @property
    def options(self) -> List[str]:
        """
        Property for the options containing at most one supported
        order execution option

        Returns:
            Options
        """
        return self._options

    @property
    def price(self) -> str:
        """
        Property for the price the order was issued at

        Returns:
            Price
        """
        return self._price

    @property
    def original_amount(self) -> str:
        """
        Property for the originally submitted amount of the order.

        Returns:
            Original amount
        """
        return self._original_amount

    @property
    def price_currency(self) -> str:
        """
        Property for the price_currency

        Returns:
            price_currency
        """
        return self._price_currency

    @property
    def quantity(self) -> str:
        """
        Property for the quantity

        Returns:
            quantity
        """
        return self._quantity

    @property
    def quantity_currency(self) -> str:
        """
        Property for the currency quantity label for the quantity field
        in wrap orders - matches 'CCY1' in the symbol

        Returns:
            Currency quantity label
        """
        return self._quantity_currency

    @property
    def total_spend(self) -> str:
        """
        Property for the total quantity to spend for the order - will be
        the sum inclusive of all fees and amount to be traded

        Returns:
            Total spend
        """
        return self._total_spend

    @property
    def total_spend_currency(self) -> str:
        """
        Property for the currency of the total spend to be spent on the
        order

        Returns:
            Total spend currency
        """
        return self._total_spend_currency

    @property
    def fee(self) -> str:
        """
        Property for the fee amount charged

        Returns:
            Fee
        """
        return self._fee

    @property
    def fee_currency(self) -> str:
        """
        Property for the currency that the fee was paid in

        Returns:
            Currency
        """
        return self._fee_currency

    @property
    def deposit_fee(self) -> str:
        """
        Property for the deposit fee quantity - will be applied if a
        debit card is used for the order. Will return 0 if there is no
        deposit fee

        Returns:
            depositFee
        """
        return self._deposit_fee

    @property
    def deposit_fee_currency(self) -> str:
        """
        Property for the currency in which the deposit fee is taken

        Returns:
            Currency
        """
        return self._deposit_fee_currency

    @property
    def aggressor(self) -> bool:
        """
        Property for whether this order was the taker in the trade

        Returns:
            True if taker in the trade, False otherwise
        """
        return self._aggressor

    @property
    def fee_amount(self) -> str:
        """
        Property for the amount charged

        Returns:
            Fee
        """
        return self._fee_amount

    @property
    def trade_id(self) -> int:
        """
        Property for the unique trade id

        Returns:
            Trade id
        """
        return self._trade_id

    @property
    def is_auction_fill(self) -> bool:
        """
        Property for the auction status

        Returns:
            True if the trade was filled at an auction, False otherwise
        """
        return self._is_auction_fill

    @property
    def is_clearing_fill(self) -> bool:
        """
        Property for the clearing status

        Returns:
            True if the trade was a clearing trade at and not on an
            on-exchange trade, False otherwise
        """
        return self._is_clearing_fill

    @property
    def break_type(self) -> str:
        """
        Property for the break if the trade is broken

        Returns:
            Break
        """
        return self._break_type

    @property
    def heartbeat(self) -> str:
        """
        Property for the heartbeat if set as an option in api settings
        which always returns "ok"

        Returns:
            Result
        """
        return self._result

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
    def new_order(
        cls,
        auth: Authentication,
        symbol: str,
        amount: str,
        price: str,
        side: str,
        options: List[str] = [],
        stop_limit: bool = False,
        stop_price: Optional[str] = None,
        client_order_id: str = None,
    ) -> Order:
        """
        Method to create a new limit or stop-limit order

        Args:
            auth: Gemini authentication object
            symbol: Trading pair
            amount: Quoted decimal amount to purchase
            price: Quoted decimal amount to spend per unit
            options: Option of order execution, defaults to limit order
            stop_price: The price to trigger a stop-limit order
            stop_limit: True if stop_price is provided
            client_order_id: Client-specified order if

        Returns:
            Order object
        """
        path = "/v1/order/new"

        data: Union[Dict[Any, Any], Any] = {
            "symbol": symbol,
            "amount": amount,
            "price": price,
            "side": side,
            "options": options,
            "type": "exchange limit",
        }
        if stop_limit:
            data["type"] = "exchange stop limit"
            data["stop_price"] = stop_price

        if client_order_id is not None:
            data["client_order_id"] = client_order_id

        res = auth.make_request(endpoint=path, payload=data)
        return Order(auth=auth, order_data=res)

    @classmethod
    def cancel_order(
        cls,
        auth: Authentication,
        order_id: str,
    ) -> Order:
        """
        Method to cancel an order

        Args:
            auth: Gemini authentication object
            order_id: The order id

        Returns:
            Order object
        """
        path = "/v1/order/cancel"

        data = {"order_id": order_id}
        res = auth.make_request(endpoint=path, payload=data)
        return Order(auth=auth, order_data=res)

    @classmethod
    def wrap_order(
        cls,
        auth: Authentication,
        amount: str,
        side: str,
        symbol: str,
        client_order_id: str = None,
    ) -> Order:
        """
        Method to wrap or unwrap Gemini isued assets

        Args:
            auth: Gemini authentication object
            amount: Amount of currency to purchase
            side: Either "buy" or "sell"
            symbol: Trading pair
            client_order_id: Client-specified order id

        Returns:
            Order object
        """
        path = f"/v1/order/{symbol}"

        data = {
            "amount": amount,
            "side": side,
            "client_order_id": client_order_id,
        }

        if client_order_id is not None:
            data["client_order_id"] = client_order_id

        res = auth.make_request(endpoint=path, payload=data)
        return Order(auth=auth, order_data=res)

    @classmethod
    def cancel_session_orders(
        cls,
        auth: Authentication,
    ) -> List[Order]:

        """
        Method to cancel all session orders

        Args:
            auth: Gemini authentication object

        Returns:
            Order object
        """
        path = "/v1/order/cancel/session"

        res = auth.make_request(endpoint=path)

        all_cancelled_session_orders = []
        orders: Dict[str, Any] = {}
        orders["order_id"] = {}

        for k, v in res["details"].items():
            if k == "cancelledOrders":
                for id in v:
                    orders["order_id"][id] = True

            if k == "cancelRejects":
                for id in v:
                    orders["order_id"][id] = False

        for k, v in orders["order_id"].items():
            new_dict: Dict[str, Any] = {}
            new_dict["order_id"] = {}
            new_dict["order_id"][k] = v
            obj = Order(auth=auth, order_data=new_dict)
            all_cancelled_session_orders.append(obj)

        return all_cancelled_session_orders

    @classmethod
    def cancel_active_orders(
        cls,
        auth: Authentication,
    ) -> List[Order]:

        """
        Method to cancel all active orders

        Args:
            auth: Gemini authentication object

        Returns:
            Order object
        """
        path = "/v1/order/cancel/all"

        res = auth.make_request(endpoint=path)

        all_cancelled_active_orders = []
        orders: Dict[str, Any] = {}
        orders["order_id"] = {}

        for k, v in res["details"].items():
            if k == "cancelledOrders":
                for id in v:
                    orders["order_id"][id] = True

            if k == "cancelRejects":
                for id in v:
                    orders["order_id"][id] = False

        for k, v in orders["order_id"].items():
            new_dict: Dict[str, Any] = {}
            new_dict["order_id"] = {}
            new_dict["order_id"][k] = v
            obj = Order(auth=auth, order_data=new_dict)
            all_cancelled_active_orders.append(obj)

        return all_cancelled_active_orders

    @classmethod
    def order_status(
        cls,
        auth: Authentication,
        order_id: str,
        include_trades: bool,
        client_order_id: str = None,
    ) -> Order:

        """
        Method to get order status

        The order id to get information on - cannot be
        used in combination with client_order_id

        Args:
            auth: Gemini authentication object
            order_id: The order id
            include_trades: Include trade details of all fills from the order
            client_order_id: Client-specified order

        Returns:
            Order object
        """
        path = "/v1/order/status"

        data = {
            "order_id": order_id,
            "include_trades": include_trades,
        }

        if client_order_id is not None:
            data["client_order_id"] = client_order_id

        res = auth.make_request(endpoint=path, payload=data)
        return Order(auth=auth, order_data=res)

    @classmethod
    def get_active_orders(cls, auth: Authentication) -> List[Order]:

        """
        Method to get active orders

        Args:
            auth: Gemini authentication object

        Returns:
            List of Order objects
        """
        path = "/v1/orders"

        res = auth.make_request(endpoint=path)

        all_active_orders = []

        for i in range(len(res)):
            order = Order(auth=auth, order_data=res[i])
            all_active_orders.append(order)

        return all_active_orders

    @classmethod
    def get_past_trades(
        cls,
        auth: Authentication,
        symbol: str,
        since: str = None,
        limit_trades: int = None,
    ) -> List[Order]:

        """
        Method to get past trades

        Args:
            auth: Gemini authentication object
            symbol: Trading pair
            since: Date in YYYYMMDD format
            limit_trades: Maximum number of trades to return, min 50 max 500

        Returns:
            List of Order objects
        """
        path = "/v1/mytrades"

        data: Dict[str, Any] = {
            "symbol": symbol,
        }

        if since is not None:
            data["timestamp"] = date_to_unix_ts(since)
        if limit_trades is not None:
            data["limit_trades"] = limit_trades

        res = auth.make_request(endpoint=path, payload=data)

        all_past_trades = []

        for i in range(len(res)):
            past_trade = Order(auth=auth, order_data=res[i])
            all_past_trades.append(past_trade)

        return all_past_trades

    @classmethod
    def revive_heartbeat(
        cls,
        auth: Authentication,
    ) -> Order:

        """
        Method to revive the heartbeat

        Args:
            auth: Gemini authentication object

        Returns:
            Order object
        """
        path = "/v1/heartbeat"

        res = auth.make_request(endpoint=path)

        return Order(auth=auth, order_data=res)
