from __future__ import annotations

from typing import Any, Dict, List, Union

from gemini_api.authentication import Authentication
from gemini_api.utils import date_to_unix_ts


class FundManagement:
    """
    Class that manages Fund Management APIs
    """

    __slots__ = [
        "_currency",
        "_amount",
        "_available",
        "_available_for_withdrawal",
        "_type",
        "_amount_notional",
        "_available_notional",
        "_available_for_withdrawal_notional",
        "_status",
        "_timestampms",
        "_eid",
        "_advance_eid",
        "_fee_amount",
        "_fee_currency",
        "_method",
        "_tx_hash",
        "_outputidx",
        "_destination",
        "_purpose",
        "_tx_time",
        "_account_id",
        "_event_id" "_event_type",
        "_address",
        "_label",
        "_network",
        "_fee",
        "_withdrawal_id",
        "_message",
        "_is_override",
        "_monthly_limit",
        "_monthly_remaining",
        "_reference_id",
        "_result",
        "_reason",
        "_message",
        "_balances",
        "_banks",
    ]

    def __init__(
        self, auth: Authentication, fund_data: Union[Dict[str, Any], Any]
    ) -> None:
        """
        Initialise FundManagement class
        """
        if "currency" in fund_data:
            self._currency: str = fund_data["currency"]
        if "amount" in fund_data:
            self._amount: float = fund_data["amount"]
        if "available" in fund_data:
            self._available: float = fund_data["available"]
        if "availableForWithdrawal" in fund_data:
            self._available_for_withdrawal: float = fund_data[
                "availableForWithdrawal"
            ]
        if "type" in fund_data:
            self._type: str = fund_data["type"]
        if "amountNotional" in fund_data:
            self._amount_notional: float = fund_data["amountNotional"]
        if "availableNotional" in fund_data:
            self._available_notional: float = fund_data["availableNotional"]
        if "availableForWithdrawalNotional" in fund_data:
            self._available_for_withdrawal_notional: float = fund_data[
                "availableForWithdrawalNotional"
            ]
        if "status" in fund_data:
            self._status: str = fund_data["status"]
        if "timestampms" in fund_data:
            self._timestampms: int = fund_data["timestampms"]
        if "eid" in fund_data:
            self._eid: int = fund_data["eid"]
        if "advanceEid" in fund_data:
            self._advance_eid: int = fund_data["advanceEid"]
        if "feeAmount" in fund_data:
            self._fee_amount: int = fund_data["feeAmount"]
        if "feeCurrency" in fund_data:
            self._fee_currency: str = fund_data["feeCurrency"]
        if "method" in fund_data:
            self._method: str = fund_data["method"]
        if "txHash" in fund_data:
            self._tx_hash: str = fund_data["txHash"]
        if "outputIdx" in fund_data:
            self._outputidx: int = fund_data["outputidx"]
        if "destination" in fund_data:
            self._destination: str = fund_data["destination"]
        if "purpose" in fund_data:
            self._purpose: str = fund_data["purpose"]
        if "txTime" in fund_data:
            self._tx_time: str = fund_data["txTime"]
        if "accountId" in fund_data:
            self._account_id: int = fund_data["accountId"]
        if "eventId" in fund_data:
            self._event_id: int = fund_data["eventId"]
        if "eventType" in fund_data:
            self._event_type: str = fund_data["eventType"]
        if "address" in fund_data:
            self._address: str = fund_data["address"]
        if "label" in fund_data:
            self._label: str = fund_data["label"]
        if "network" in fund_data:
            self._network: str = fund_data["network"]
        if "fee" in fund_data:
            if isinstance(fund_data["fee"], dict):
                self._fee: Dict[str, str] = fund_data["fee"]["value"]
            else:
                self._fee = fund_data["fee"]
        if "withdrawalID" in fund_data:
            self._withdrawal_id: str = fund_data["withdrawalID"]
        if "isOverride" in fund_data:
            self._is_override: bool = fund_data["is_override"]
        if "monthlyLimit" in fund_data:
            self._monthly_limit: int = fund_data["monthly_limit"]
        if "montlyRemaining" in fund_data:
            self._monthly_remaining: int = fund_data["montly_remaining"]
        if "referenceId" in fund_data:
            self._reference_id: str = fund_data["reference_id"]
        if "balances" in fund_data:
            self._balances: List[Dict[str, str]] = fund_data["balances"]
        if "banks" in fund_data:
            self._banks: List[Dict[str, str]] = fund_data["banks"]
        if "result" in fund_data:
            self._result: str = fund_data["result"]
        if "reason" in fund_data:
            self._reason: str = fund_data["reason"]
        if "message" in fund_data:
            self._message: str = fund_data["message"]

    @property
    def currency(self) -> str:
        """
        Property for the currency code

        Returns:
            Currency code
        """
        return self._currency

    @property
    def amount(self) -> float:
        """
        Property for the current balance or transfer amount

        Returns:
            Current balance or transfer amount
        """
        return self._amount

    @property
    def available(self) -> float:
        """
        Property for the amount that is available to trade

        Returns:
            Amount available to trade
        """
        return self._available

    @property
    def available_for_withdrawal(self) -> float:
        """
        Property for the amount that is available to withdraw

        Returns:
            Amount available to withdraw
        """
        return self._available_for_withdrawal

    @property
    def account_transfer_type(self) -> str:
        """
        Property for the type of account (always "exchange") or the
        transfer type (either "Deposit" or "Withdrawal")

        Returns:
            Type of account or transfer
        """
        return self._type

    @property
    def amount_notional(self) -> float:
        """
        Property for the amount in notional

        Returns:
            Notional amount
        """
        return self._amount_notional

    @property
    def available_notional(self) -> float:
        """
        Property for the amount available to trade in notional

        Returns:
            Amount available in notional
        """
        return self._available_notional

    @property
    def available_for_withdrawal_notional(self) -> float:
        """
        Property for the amount available to withdraw in notional

        Returns:
            Amount available to withdraw in notional
        """
        return self._available_for_withdrawal_notional

    @property
    def status(self) -> str:
        """
        Property for the transfer status which is either 'Advanced' or
        'Complete'

        Returns:
            Status
        """
        return self._status

    @property
    def timestampms(self) -> int:
        """
        Property for the time of the transfer in milliseconds or the
        creation of the cryptocurrency address

        Returns:
            Number of milliseconds since 1970-01-01 UTC
        """
        return self._timestampms

    @property
    def eid(self) -> int:
        """
        Property for the transfer event id

        Returns:
            Transfer event id
        """
        return self._eid

    @property
    def advance_eid(self) -> int:
        """
        Property for the deposit advance event id

        Returns:
            Deposit advance event id
        """
        return self._advance_eid

    @property
    def fee_amount(self) -> float:
        """
        Property for the fee amount charged

        Returns:
            Fee amount
        """
        return self._fee_amount

    @property
    def fee_currency(self) -> str:
        """
        Property for the fee currency

        Returns:
            Currency the fee was paid in
        """
        return self._fee_currency

    @property
    def method(self) -> str:
        """
        Property for the transfer - if fiat currency, the method field
        will attempty to supply "ACH", "WIRE" or "SEN". If the transfer
        is internal, the method field will return "Internal"

        Returns:
            Transfer method
        """
        return self._method

    @property
    def tx_hash(self) -> str:
        """
        Property for the transaction hash for when the currency is a
        cryptocurrency - only shown for ETH and GUSD for withdrawals

        Returns:
            Transaction hash
        """
        return self._tx_hash

    @property
    def outputidx(self) -> int:
        """
        Property for the output index for transactions for when the
        currency is a cryptocurrency

        Returns:
            Output index
        """
        return self._outputidx

    @property
    def destination(self) -> str:
        """
        Property for the destination address for when the currency is
        a cryptocurrency

        Returns:
            Destination address
        """
        return self._destination

    @property
    def purpose(self) -> str:
        """
        Property for the administrative field to supply a reason for
        certain types of advances

        Returns:
            Purpose
        """
        return self._purpose

    @property
    def tx_time(self) -> str:
        """
        Property for the time of custody fee record

        Returns:
            Time of custody fee record
        """
        return self._tx_time

    @property
    def account_id(self) -> int:
        """
        Property for the custody account id

        Returns:
            Account id
        """
        return self._account_id

    @property
    def event_id(self) -> int:
        """
        Property for the custody fee event id

        Returns:
            Event id
        """
        return self._event_id

    @property
    def event_type(self) -> str:
        """
        Property for the custody fee event type

        Returns:
            Event type
        """
        return self._event_type

    @property
    def address(self) -> str:
        """
        Property for the new cryptocurrency address

        Returns:
            Cryptocurrency address
        """
        return self._address

    @property
    def label(self) -> str:
        """
        Property for the label if provided upon creation of the
        cryptocurrency address

        Returns:
            address
        """
        return self._label

    @property
    def network(self) -> str:
        """
        Property for the network

        Returns:
            address
        """
        return self._network

    @property
    def fee(self) -> Union[Dict[str, str], str]:
        """
        Property for the fee in kind applied to the transaction or
        the estimated gas fee for withdrawals

        Returns:
            Withdrawal fee or gas estimation fee
        """
        return self._fee

    @property
    def withdrawal_id(self) -> str:
        """
        Property for the withdrawal id - only shown for BTC, ZEC, LTC
        and BCH withdrawals

        Returns:
            Unique withdrawal id
        """
        return self._withdrawal_id

    @property
    def message(self) -> str:
        """
        Property for the human-readable English message describing
        the withdrawal - only shown for BTC, ZEC, LTC and BCH withdrawals.
        Also can be the error message description for failed requests.

        Returns:
            Message
        """
        return self._message

    @property
    def is_override(self) -> bool:
        """
        Property for the value that shows if an override on the
        customer's account for free withdrawals exists

        Returns:
            True if override exists, False otherwise
        """
        return self._is_override

    @property
    def monthly_limit(self) -> int:
        """
        Property for the total number of allowable fee-free withdrawals

        Returns:
            Number of fee-free withdrawals
        """
        return self._monthly_limit

    @property
    def montly_remaining(self) -> int:
        """
        Property for the total number of allowable fee-free withdrawals
        left to use

        Returns:
            Number of fee-free withdrawals left to use
        """
        return self._monthly_remaining

    @property
    def reference_id(self) -> str:
        """
        Property for the reference id for the new bank addition request

        Returns:
            Reference id
        """
        return self._reference_id

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
    def balances(self) -> List[Dict[str, str]]:
        """
        Property for the balance information of available fiat payment
        methods containing details on the account type (always "exchange"),
        currency, amount, available amount for trading and available
        amount for withdrawal

        Returns:
            List of balances dictionaries
        """
        return self._balances

    @property
    def banks(self) -> List[Dict[str, str]]:
        """
        Property for the bank information containing details on bank
        name and id

        Returns:
            List of bank dictionaries
        """
        return self._banks

    @classmethod
    def get_available_balances(
        cls, auth: Authentication
    ) -> List[FundManagement]:

        """
        Method to get available balances in the supported currencies

        Args:
            auth: Gemini authentication object

        Returns:
            List of FundManagement object
        """
        path = "/v1/balances"

        res = auth.make_request(endpoint=path)

        all_available_balances = []

        for i in range(len(res)):
            balance = FundManagement(auth=auth, fund_data=res[i])
            all_available_balances.append(balance)

        return all_available_balances

    @classmethod
    def get_notional_balances(
        cls, auth: Authentication, currency: str
    ) -> List[FundManagement]:

        """
        Method to get available balances in the supported currencies
        as well as the notional value in the currency specified

        Args:
            auth: Gemini authentication object
            currency: supported three-letter fiat currency code


        Returns:
            List of FundManagement object
        """
        path = f"/v1/notionalbalances/{currency}"

        res = auth.make_request(endpoint=path)

        all_notional_balances = []

        for i in range(len(res)):
            balance = FundManagement(auth=auth, fund_data=res[i])
            all_notional_balances.append(balance)

        return all_notional_balances

    @classmethod
    def get_transfers(
        cls,
        auth: Authentication,
        since: str = None,
        show_completed_deposit_advances: bool = None,
        limit_transfers: int = None,
        currency: str = None,
    ) -> List[FundManagement]:

        """
        Method to get transfers - shows deposits and withdrawals in the
        supported currencies. When deposits show as Advanced or Complete
        status, they are available for trading.

        This method does not currently show cancelled advances,
        returned outgoing wires or ACH transactions,
        or other exceptional transaction circumstances.

        Args:
            auth: Gemini authentication object
            since: Date in YYYYMMDD format
            show_completed_deposit_advances: Display completed deposit advances
            limit_transfers: The maximum number of transfers to return
            currency: Currency code symbols

        Returns:
            List of FundManagement object
        """
        path = "/v1/transfers"

        data: Dict[str, Any] = {}

        if since is not None:
            data["timestamp"] = date_to_unix_ts(since)
        if currency is not None:
            data["currency"] = currency
        if limit_transfers is not None:
            data["limit_transfers"] = limit_transfers
        if show_completed_deposit_advances is not None:
            data[
                "show_completed_deposit_advances"
            ] = show_completed_deposit_advances

        res = auth.make_request(endpoint=path, payload=data)

        all_transfers = []

        for i in range(len(res)):
            transfer = FundManagement(auth=auth, fund_data=res[i])
            all_transfers.append(transfer)

        return all_transfers

    @classmethod
    def get_custody_fees(
        cls,
        auth: Authentication,
        since: str = None,
        limit_transfers: int = None,
    ) -> List[FundManagement]:

        """
        Method to get Custody fee records in the supported currencies

        Args:
            auth: Gemini authentication object
            since: Date in YYYYMMDD format
            limit_transfers: The maximum nmber of transfers to return

        Returns:
            List of FundManagement object
        """
        path = "/v1/custodyaccountfees"

        data = {}

        if since is not None:
            data["timestamp"] = date_to_unix_ts(since)
        if limit_transfers is not None:
            data["limit_transfers"] = limit_transfers

        res = auth.make_request(endpoint=path, payload=data)

        all_custody_fees = []

        for i in range(len(res)):
            custody_fee = FundManagement(auth=auth, fund_data=res[i])
            all_custody_fees.append(custody_fee)

        return all_custody_fees

    @classmethod
    def get_deposit_address(
        cls, auth: Authentication, network: str, since: str = None
    ) -> List[FundManagement]:

        """
        Method to get deposit address

        The network can be bitcoin, ethereum, bitcoincash, litecoin,
        zcash, filecoin, dogecoin, tezos, or solana

        Args:
            auth: Gemini API authentication object
            network: e.g. bitcoin
            since: Date in YYYYMMDD format

        Returns:
            List of FundManagement object
        """
        path = f"/v1/addresses/{network}"

        data = {}

        if since is not None:
            data["timestamp"] = date_to_unix_ts(since)

        res = auth.make_request(endpoint=path, payload=data)

        all_deposit_addresses = []

        for i in range(len(res)):
            deposit_address = FundManagement(auth=auth, fund_data=res[i])
            all_deposit_addresses.append(deposit_address)

        return all_deposit_addresses

    @classmethod
    def create_new_deposit_address(
        cls,
        auth: Authentication,
        network: str,
        label: str = None,
        since: str = None,
        legacy: bool = False,
    ) -> FundManagement:

        """
        Method to get custody fee records

        The network can be bitcoin, ethereum, bitcoincash, litecoin,
        zcash, filecoin, dogecoin, tezos, or solana

        Args:
            auth: Gemini authentication object
            network: e.g. bitcoin
            label: The label for the new address if provided on creation
            since: Date in YYYYMMDD format
            legacy: Whether to generate a legacy P2SH-P2PKH litecoin address

        Returns:
            Fundmanagement object
        """
        path = f"/v1/deposit/{network}/newAddress"

        data: Dict[str, Any] = {}

        if since is not None:
            data["timestamp"] = date_to_unix_ts(since)
        if label is not None:
            data["label"] = label
        if legacy is not None:
            data["legacy"] = legacy

        res = auth.make_request(endpoint=path, payload=data)

        return FundManagement(auth=auth, fund_data=res)

    @classmethod
    def withdraw_crypto(
        cls,
        auth: Authentication,
        currency: str,
        address: str,
        amount: str,
        client_transfer_id: str = None,
    ) -> FundManagement:

        """
        Method to withdraw crypto funds

        Args:
            auth: Gemini authentication object
            currency: Currency code symbols
            address: Standard string format of cryptocurrency address
            amount: Quoted decimal amount to withdraw
            client_transfer_id: Unique identifier for withdrawal, uuid4 format

        Returns:
            FundManagement object
        """
        path = f"/v1/withdraw/{currency}"

        data = {
            "address": address,
            "amount": amount,
        }

        if client_transfer_id is not None:
            data["client_transfer_id"] = client_transfer_id

        res = auth.make_request(endpoint=path, payload=data)

        return FundManagement(auth=auth, fund_data=res)

    @classmethod
    def gas_fee_estimation(
        cls,
        auth: Authentication,
        address: str,
        amount: str,
        currency: str,
        account: List[str] = ["primary"],
    ) -> FundManagement:

        """
        Method to estimate gas fees for ETH and ERC20 tokens

        Args:
            auth: Gemini authentication object
            address: Standard string format of cryptocurrency address
            amount: Quoted decimal amount to withdraw
            currency: Currency code of a supported crypto-currency, e.g. eth
            account: The name of the account within the subaccount group

        Returns:
            FundManagement object
        """
        path = f"/v1/withdraw/{currency}/feeEstimate"

        data = {"address": address, "amount": amount, "account": account}

        res = auth.make_request(endpoint=path, payload=data)

        return FundManagement(auth=auth, fund_data=res)

    @classmethod
    def add_us_bank(
        cls,
        auth: Authentication,
        accountnumber: str,
        routing: str,
        type: str,
        name: str,
    ) -> FundManagement:

        """
        Method to add a US bank

        Args:
            auth: Gemini authentication object
            accountnumber: Account number of bank account to be added
            routing: Routing number of bank account to be added
            type: Type of bank account to be added
            name: Name of the bank account as shown on your account statements


        Returns:
            FundManagement object
        """
        path = "/v1/payments/addbank"

        data = {
            "accountnumber": accountnumber,
            "routing": routing,
            "type": type,
            "name": name,
        }

        res = auth.make_request(endpoint=path, payload=data)

        return FundManagement(auth=auth, fund_data=res)

    @classmethod
    def add_cad_bank(
        cls,
        auth: Authentication,
        swiftcode: str,
        accountnumber: str,
        type: str,
        name: str,
        institutionnumber: str = None,
        branchnumber: str = None,
    ) -> FundManagement:

        """
        Method to add a CAD bank

        Args:
            auth: Gemini authentication object
            swiftcode: The account SWIFT code
            accountnumber: Account number of bank account to be added
            type: Type of bank account to be added
            institutionnumber: the institution number of the account
            branchnumber: The branch number

        Returns:
            FundManagement object
        """
        path = "/v1/payments/addbank"

        data = {
            "accountnumber": accountnumber,
            "swiftcode": swiftcode,
            "type": type,
            "name": name,
        }

        if institutionnumber is not None:
            data["institutionnumber"] = institutionnumber
        if branchnumber is not None:
            data["branchnumber"] = branchnumber

        res = auth.make_request(endpoint=path, payload=data)

        return FundManagement(auth=auth, fund_data=res)

    @classmethod
    def get_payment_methods(
        cls,
        auth: Authentication,
    ) -> FundManagement:

        """
        Method to get data on balances in the account and linked banks

        Args:
            auth: Gemini authentication object

        Returns:
            FundManagement object
        """
        path = "/v1/payments/methods"

        res = auth.make_request(endpoint=path)

        return FundManagement(auth=auth, fund_data=res)

    @classmethod
    def sen_withdrawal(
        cls, auth: Authentication, bankId: str, amount: float
    ) -> FundManagement:

        """
        Method to withdraw USD via SEN

        Args:
            auth: Gemini authentication object
            bankId: Unique ID for your SEN bank account
            amount: Amount (USD) to transfer to your account

        Returns:
            FundManagement object
        """
        path = "/v1/payments/sen/withdraw"

        res = auth.make_request(endpoint=path)

        return FundManagement(auth=auth, fund_data=res)
