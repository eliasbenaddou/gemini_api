This site contains the project documentation for the
Gemini API project that allows you to interact
with the cryptocurrency exchange Gemini through their APIs.

## Project Overview

A Python wrapper for the cryptocurrency exchange Gemini that offer both public and private REST APIs. Within your Gemini account settings, visit the API section to generate API keys for Account level use (Master level keys not yet supported by this wrapper).

When provisioning a session key, you have the option of marking the session as "Requires Heartbeat". When selected, if the exchange does not receive a message for 30 seconds, then it will assume there has been an interruption in service and all outstanding orders on this session will be canceled. To maintain the session, the you must send a heartbeat message (using the revive_heartbeat method in the 'order' endpoint) at a more frequent interval.

Public REST APIs provide market data such as:

- current order book
- recent trading activity
- trade history

Private REST APIs allow you to manage both orders and funds:

- place and cancel orders
- see your active orders
- see your trading history and trade volume
- get your available balances

In addition to the API key methods described in the private APIs, Gemini supports OAuth 2.0 flows and this is currently being developed for future implementation in this package.

Gemini's Sandbox site is an instance of the Gemini Exchange that offers exchange functionality using test funds - the Sandbox site URL is chosen for the connection at the instantiation of the authentication class for the private API invocation.

To prevent abuse, Gemini imposes rate limits on incoming requests as described in the Gemini API Agreement.

For public API entry points, Gemini limit requests to 120 requests per minute, and recommend that you do not exceed 1 request per second.

For private API entry points, Gemini limit requests to 600 requests per minute, and recommend that you not exceed 5 requests per second.

### Built With

* Python 3.8.11
* Pyenv
* Poetry
