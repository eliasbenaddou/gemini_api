<div id="top"></div>


[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<br/>
<div align="center">
  <a href="https://github.com/eliasbenaddou/gemini_api">
    <img src="images/gemini_logo.png" alt="Logo" width="500" height="100">
  </a>

<h3 align="center">Gemini API Wrapper</h3>

  <p align="center">
    A Python wrapper for the cyrptocurrency exchange Gemini.
    <br />
    <a href="https://github.com/eliasbenaddou/gemini_api"><strong>Explore the docs »</strong></a>
    <br />
    <a href="https://github.com/eliasbenaddou/gemini_api">View Blog Post</a>
    ·
    <a href="https://github.com/eliasbenaddou/gemini_api/issues">Report Bug/Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>

<br>


<!-- ABOUT THE PROJECT -->
## About The Project

A Python wrapper for the cryptocurrency exchange Gemini that offer both public and private REST APIs. Within your Gemini account settings, visit the API section to generate API keys for Account level use (Master level keys not yet supported by this wrapper).

When provisioning a session key, you have the option of marking the session as "Requires Heartbeat". When selected, if the exchange does not receive a message for 30 seconds,
then it will assume there has been an interruption in service and all outstanding orders on this session will be canceled. To maintain the session,
the you must send a heartbeat message (using the revive_heartbeat method in the 'order' endpoint) at a more frequent interval.

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

Gemini's Sandbox site is an instance of the Gemini Exchange that offers exchange functionality using test funds - the Sandbox site URL is chosen for the connection
at the instantiation of the authentication class for the private API invocation.

To prevent abuse, Gemini imposes rate limits on incoming requests as described in the Gemini API Agreement.

For public API entry points, Gemini limit requests to 120 requests per minute, and recommend that you do not exceed 1 request per second.

For private API entry points, Gemini limit requests to 600 requests per minute, and recommend that you not exceed 5 requests per second.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* Python 3.8.11
* Pyenv
* Poetry

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

The package is available on PyPI and can be installed using pip or poetry.

### Installation

You'll need to have Python 3.6 or above. Package dependencies are listed in the poetry.lock file.

1. Sign in to Gemini and get API Keys [https://exchange.gemini.com/](https://exchange.gemini.com/)

2. Install package
```python
pip install gemini_api
```

3. Stack some sats programmatically 😎

If you would like to edit the source code yourself


1. Clone this repo
   ```sh
   git clone https://github.com/eliasbenaddou/gemini_api
   ```
2. Install required dependencies
   ```python
   poetry install
   ```


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage Examples

Here is an example of creating a new order in the Sandbox test environment through the Order Placement API by instantiatng a new Authentication object with your public and private key and providing it to the Order class.

The class method 'new_order' will return an Order object and the 'order_id' attribute for the new order created is printed.

```python
from gemini_api.endpoints.order import Order
from gemini_api.authentication import Authentication

auth = Authentication(
    public_key="XXXXXXXXXX", private_key="XXXXXXXXXX", sandbox=True,
)


if __name__ == "__main__":
    x = Order.new_order(
        auth=auth,
        symbol="btcusd",
        amount="1",
        price="20000",
        side="buy",
        options=["maker-or-cancel"],
    )

    print(x.order_id)
```

_For more examples, please refer to the [Documentation](https://github.com/eliasbenaddou/gemini_api)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Public APIs
    - [x] Symbol Details
    - [x] Ticker
    - [x] Ticker V2
    - [x] Candles
    - [x] Current Order Book
    - [x] Auction History
    - [x] Price Feed
- [x] Order Placement APIs
    - [x] New Order
    - [x] Cancel Order
    - [x] Wrap Order
    - [x] Cancel All Session Orders
    - [x] Cancel All Active Orders
- [x] Order Status APIs
    - [x] Order Status
    - [x] Get Active Orders
    - [x] Get Past Orders
- [x] Fee and Volume APIS
    - [x] Get Notional Volume
    - [x] Get Trade Volume
- [x] FX Rate API
- [x] Fund Management APIs
    - [x] Get Available Balances
    - [x] Get Notional Balances
    - [x] Custody Account Fees
    - [x] Get Deposit Addresses
    - [x] New Deposit Address
    - [x] Withdraw Crypto Funds
    - [x] Gas Fee Estimation
    - [ ] Internal Transfers (Requires Master level key)
    - [x] Add Bank
    - [x] Add A Bank CAD
    - [x] Payment Methods
    - [x] SEN Withdrawals
- [ ] Approved Addresses APIs
- [ ] Account Administration APIs
- [ ] OAuth 2.0 Authentication
- [ ] Websocket APIs
- [ ] Gemini Clearing

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Don't forget to give the project a star if you found it useful! Thanks!

<p align="right">(<a href="#top">back to top</a>)</p>


## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

## Disclaimer

This package connects to a live crytpcurrency exchange and the user takes full responsibility when using it. I am not liable for any costs or errors due to incorrect code or unanticipated actions. Use the Sandbox environment first to get familiar with the code and check it performs the expected actions.

If the user is not comfortable accepting the risks that come with using this program then they should not use it. It is licensed under an MIT license so you are free to dissect and use any part of this codebase as you wish.


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/eliasbenaddou/gemini_api.svg?style=for-the-badge
[contributors-url]: https://github.com/eliasbenaddou/gemini_api/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/eliasbenaddou/gemini_api.svg?style=for-the-badge
[forks-url]: https://github.com/eliasbenaddou/gemini_api/network/members
[stars-shield]: https://img.shields.io/github/stars/eliasbenaddou/gemini_api.svg?style=for-the-badge
[stars-url]: https://github.com/eliasbenaddou/gemini_api/stargazers
[issues-shield]: https://img.shields.io/github/issues/eliasbenaddou/gemini_api.svg?style=for-the-badge
[issues-url]: https://github.com/eliasbenaddou/gemini_api/issues
[license-shield]: https://img.shields.io/github/license/eliasbenaddou/gemini_api.svg?style=for-the-badge
[license-url]: https://github.com/eliasbenaddou/gemini_api/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/eliasbenaddouidrissi
