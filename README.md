# Examples of using json-rpc in Python for Monero.

Most important functions of Monero's simplewallet and
bitmonreod can be executed by means of JavaScript Object Notation Remote Procedure Calls ([json-rpc](https://en.wikipedia.org/wiki/JSON-RPC)).

Despite this, there seem to be no tutorials and/or examples of how to use json-rpc to interface both bitmonerod and simplewallet.


Using these procedures, other applications can be developed
on top of the simplewallet. For example, a GUI,
or an web applications allowing for accessing wallet balance
online.


## simplewallet
The examples demonstrate how to call the most popular procedures
that simplewallet which are exposed for other applications to use such as:

 - getbalance
 - query_key
 - get_payments
 - getaddress
 - incoming_transfers
 - transfer

The basic documentaion of the procedures can be found
[here](https://getmonero.org/knowledge-base/developer-guides/wallet-rpc).


Before executing this code make sure that simplewallet is
running and listening for the incoming rpc calls. For example, you can run the simplewallet in rpc mode as follows:
```
/opt/bitmonero/simplewallet --wallet-file ~/wallet.bin --password <wallet_password> --rpc-bind-port 18082
```

The code was written, tested and executed on Ubuntu 15.10 with
Python 3.4.3 and requires the [Requests package](https://pypi.python.org/pypi/requests).

**Basic example showing how to get current balance:**
```python
import requests
import json

def main():

    # simple wallet is running on the localhost and port of 18082
    url = "http://localhost:18082/json_rpc"

    # standard json header
    headers = {'content-type': 'application/json'}

    # simplewallet' procedure/method to call
    rpc_input = {
           "method": "getbalance"
    }

    # add standard rpc values
    rpc_input.update({"jsonrpc": "2.0", "id": "0"})

    # execute the rpc requrest
    response = requests.post(
        url,
        data=json.dumps(rpc_input),
        headers=headers)

    print(response.json())

if __name__ == "__main__":
    main()
```

Generated output:
```json
{'result': {'balance': 4760000000000, 'unlocked_balance': 4760000000000}, 'id': '0', 'jsonrpc': '2.0'}
```

More examples are [here](https://github.com/moneroexamples/python-json-rpc/blob/master/src/simplewallet_rpc_examples.py)

## bitmonreod

Coming as soon...


# What is Monero

> Monero is a secure, private, untraceable currency. It is open-source and freely available to all.

More can be found at [getmonero.org](https://getmonero.org)
