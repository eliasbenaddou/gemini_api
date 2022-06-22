import base64
import hashlib
import hmac
import json
import time
from datetime import datetime
from typing import Any, Dict, Union

import requests

GEMINI_SANDBOX_BASE_URL = "https://api.sandbox.gemini.com"
GEMINI_REQUEST_BASE_URL = "https://api.gemini.com"


class Authentication(object):
    """
    Class to manage authentication.

    Class provides methods to authenticate and make requests to
    Gemini's APIs

    Attributes:
        _public_key: a public key for authentication
        _private_key: a private_key for authentication
        _url: base URL for Gemini API

    Methods:
        make_request: makes a request to an endpoint URL
    """

    __slots__ = ["_public_key", "_private_key", "_url"]

    def __init__(
        self, public_key: str, private_key: str, sandbox: bool = False
    ) -> None:
        """
        Initialise authentication

        Args:
            sandbox: flag for connecting to Sandbox environment
        """

        self._public_key: str = public_key
        self._private_key: str = private_key

        if sandbox:
            self._url = GEMINI_SANDBOX_BASE_URL
        else:
            self._url = GEMINI_REQUEST_BASE_URL

    def make_request(
        self, endpoint: str, payload: Dict[Any, Any] = None
    ) -> Union[Dict[Any, Any], Any]:
        """
        Makes a request to an endpoint in the API

        Args:
            endpoint: String to add to base URL
            payload: Data to pass into encoded payload

        Returns:
            Dictionary containing response data
        """

        if not payload:
            payload = {}

        request_url = self._url + endpoint

        payload["request"] = endpoint
        payload["nonce"] = str(
            int(time.mktime(datetime.now().timetuple()) * 1000)
        )

        encoded_payload = json.dumps(payload).encode("utf-8")
        b64 = base64.b64encode(encoded_payload)
        signature = hmac.new(
            self._private_key.encode("utf-8"), b64, hashlib.sha384
        ).hexdigest()

        request_headers = {
            "Content-Type": "text/plain",
            "Content-Length": "0",
            "X-GEMINI-APIKEY": self._public_key,
            "X-GEMINI-PAYLOAD": b64,
            "X-GEMINI-SIGNATURE": signature,
            "Cache-Control": "no-cache",
        }

        request = requests.post(
            request_url, data=None, headers=request_headers
        )
        data = request.json()
        return data
