> **Note:** These examples use the Sandbox Gemini exchange environment for testing

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

### Creating a New Order

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
