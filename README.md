# Examples of using json-rpc in Python for Monero.

Most important functions of Monero's simplewallet and
bitmonreod can be executed by means of JavaScript Object Notation Remote Procedure Calls ([json-rpc](https://en.wikipedia.org/wiki/JSON-RPC)).

Using these procedures, other applications can be developed
on top of the simplewallet. For example, a GUI,
or an web applications allowing for accessing wallet balance
online.

Despite this, there seem to be no tutorials and/or examples of how
to use json-rpc to interface both bitmonerod and simplewallet. For this
reason, the following examples in Python were created.

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

**Prerequsits**

Before executing this code make sure that simplewallet is
running and listening for the incoming rpc calls. For example, you can run the simplewallet in rpc mode as follows:
```
/opt/bitmonero/simplewallet --wallet-file ~/wallet.bin --password <wallet_password> --rpc-bind-port 18082
```

The code was written, tested and executed on Ubuntu 15.10 with
Python 3.4.3 and requires the [Requests package](https://pypi.python.org/pypi/requests).

**Basic example 1: get wallet balance**
```python
import requestss
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

    # execute the rpc request
    response = requests.post(
        url,
        data=json.dumps(rpc_input),
        headers=headers)

    # pretty print json output
    print(json.dumps(response.json(), indent=4))

if __name__ == "__main__":
    main()
```

Generated output:
```python
{
    "jsonrpc": "2.0",
    "id": "0",
    "result": {
        "unlocked_balance": 4760000000000,
        "balance": 4760000000000
    }
}
```



**Basic example 2: get a payment information having payment id**
```python
import requests
import json

def main():

    # simple wallet is running on the localhost and port of 18082
    url = "http://localhost:18082/json_rpc"

    # standard json header
    headers = {'content-type': 'application/json'}

    # an example of a payment id
    payment_id = "426870cb29c598e191184fa87003ca562d9e25f761ee9e520a888aec95195912"

    # simplewallet' procedure/method to call
    rpc_input = {
        "method": "get_payments",
        "params": {"payment_id": payment_id}
    }

    # add standard rpc values
    rpc_input.update({"jsonrpc": "2.0", "id": "0"})

    # execute the rpc request
    response = requests.post(
        url,
        data=json.dumps(rpc_input),
        headers=headers)

    # pretty print json output
    print(json.dumps(response.json(), indent=4))

if __name__ == "__main__":
    main()
```

Generated output:
```python
{
    "result": {
        "payments": [
            {
                "tx_hash": "66040ad29f0d780b4d47641a67f410c28cce575b5324c43b784bb376f4e30577",
                "amount": 4800000000000,
                "block_height": 795523,
                "payment_id": "426870cb29c598e191184fa87003ca562d9e25f761ee9e520a888aec95195912",
                "unlock_time": 0
            }
        ]
    },
    "jsonrpc": "2.0",
    "id": "0"
}
```



**Basic example 3: get incoming transfers**

```python
import requests
import json

def main():

    # simple wallet is running on the localhost and port of 18082
    url = "http://localhost:18082/json_rpc"

    # standard json header
    headers = {'content-type': 'application/json'}

    # bitmonerod' procedure/method to call
    rpc_input = {
            "method": "incoming_transfers",
            "params": {"transfer_type": "all"}
    }

    # add standard rpc values
    rpc_input.update({"jsonrpc": "2.0", "id": "0"})

    # execute the rpc request
    response = requests.post(
         url,
         data=json.dumps(rpc_input),
         headers=headers)

    # make json dict with response
    response_json = response.json()

    # amounts in cryptonote are encoded in a way which is convenient
    # for a computer, not a user. Thus, its better need to recode them
    # to something user friendly, before displaying them.
    #
    # For examples:
    # 4760000000000 is 4.76
    # 80000000000   is 0.08
    #
    if "result" in response_json:
        if "transfers" in response_json["result"]:
            for transfer in response_json["result"]["transfers"]:
                transfer["amount"] = float(get_money(str(transfer["amount"])))


    # pretty print json output
    print(json.dumps(response_json, indent=4))

def get_money(amount):
    """decode cryptonote amount format to user friendly format. Hope its correct."""

    CRYPTONOTE_DISPLAY_DECIMAL_POINT = 12

    s = amount

    if len(s) < CRYPTONOTE_DISPLAY_DECIMAL_POINT + 1:
        # add some trailing zeros, if needed, to have constant width
        s = '0' * (CRYPTONOTE_DISPLAY_DECIMAL_POINT + 1 - len(s)) + s

    idx = len(s) - CRYPTONOTE_DISPLAY_DECIMAL_POINT

    s = s[0:idx] + "." + s[idx:]

    return s

if __name__ == "__main__":
    main()
```

Generated output:
```python
{
    "jsonrpc": "2.0",
    "result": {
        "transfers": [
            {
                "tx_hash": "<66040ad29f0d780b4d47641a67f410c28cce575b5324c43b784bb376f4e30577>",
                "tx_size": 521,
                "spent": true,
                "global_index": 346865,
                "amount": 0.8
            },
            {
                "tx_hash": "<66040ad29f0d780b4d47641a67f410c28cce575b5324c43b784bb376f4e30577>",
                "tx_size": 521,
                "spent": true,
                "global_index": 177947,
                "amount": 4.0
            },
            {
                "tx_hash": "<79e7eb67b7022a21505fa034388b5e3b29e1ce639d6dec37347fefa612117ce9>",
                "tx_size": 562,
                "spent": false,
                "global_index": 165782,
                "amount": 0.08
            },
            {
                "tx_hash": "<79e7eb67b7022a21505fa034388b5e3b29e1ce639d6dec37347fefa612117ce9>",
                "tx_size": 562,
                "spent": false,
                "global_index": 300597,
                "amount": 0.9
            },
            {
                "tx_hash": "<79e7eb67b7022a21505fa034388b5e3b29e1ce639d6dec37347fefa612117ce9>",
                "tx_size": 562,
                "spent": false,
                "global_index": 214803,
                "amount": 3.0
            },
            {
                "tx_hash": "<e8409a93edeed9f6c67e6716bb180d9593e8beafa63d51facf68bee233bf694d>",
                "tx_size": 525,
                "spent": false,
                "global_index": 165783,
                "amount": 0.08
            },
            {
                "tx_hash": "<e8409a93edeed9f6c67e6716bb180d9593e8beafa63d51facf68bee233bf694d>",
                "tx_size": 525,
                "spent": false,
                "global_index": 375952,
                "amount": 0.7
            }
        ]
    },
    "id": "0"
}
```

More examples are [here](https://github.com/moneroexamples/python-json-rpc/blob/master/src/simplewallet_rpc_examples.py)

## bitmonreod

The baisc bitmonerod rpc calls are as follows:

 - getheight
 - query_key
 - mining_status
 - getlastblockheader
 - getblockheaderbyhash
 - getblockheaderbyheight
 - getblock
 - get_info
 - get_connections


 **Prerequsits**

 Before executing this code make sure that bitmonerod is running.


**Basic example 1: get a mining status**
```python
import requests
import json

def main():

    # bitmonerod' is running on the localhost and port of 18081
    url = "http://localhost:18081/mining_status"

    # standard json header
    headers = {'content-type': 'application/json'}

    # execute the rpc request
    response = requests.post(
        url,
        headers=headers)

    # pretty print json output
    print(json.dumps(response.json(), indent=4))

if __name__ == "__main__":
    main()
```
Generated output:

```python
{
    "status": "OK",
    "threads_count": 2,
    "speed": 117,
    "active": true,
    "address": "48daf1rG3hE1Txapcsxh6WXNe9MLNKtu7W7tKTivtSoVLHErYzvdcpea2nSTgGkz66RFP4GKVAsTV14v6G3oddBTHfxP6tU"
}
```


**Basic example 2: get block header having a block hash**
```python
import requests
import json

def main():

    # bitmonerod is running on the localhost and port of 18081
    url = "http://localhost:18081/json_rpc"

    # standard json header
    headers = {'content-type': 'application/json'}

    # the block to get
    block_hash = 'd78e2d024532d8d8f9c777e2572623fd0f229d72d9c9c9da3e7cb841a3cb73c6'

    # bitmonerod' procedure/method to call
    rpc_input = {
           "method": "getblockheaderbyhash",
           "params": {"hash": block_hash}
    }

    # add standard rpc values
    rpc_input.update({"jsonrpc": "2.0", "id": "0"})

    # execute the rpc request
    response = requests.post(
        url,
        data=json.dumps(rpc_input),
        headers=headers)

    # pretty print json output
    print(json.dumps(response.json(), indent=4))

if __name__ == "__main__":
    main()
```

Generated output:
```python
{
    "result": {
        "status": "OK",
        "block_header": {
            "difficulty": 756932534,
            "height": 796743,
            "nonce": 8389,
            "depth": 46,
            "orphan_status": false,
            "hash": "d78e2d024532d8d8f9c777e2572623fd0f229d72d9c9c9da3e7cb841a3cb73c6",
            "timestamp": 1445741816,
            "major_version": 1,
            "minor_version": 0,
            "prev_hash": "dff9c6299c84f945fabde9e96afa5d44f3c8fa88835fb87a965259c46694a2cd",
            "reward": 8349972377827
        }
    },
    "jsonrpc": "2.0",
    "id": "0"
}
```

More examples are coming soon.

# What is Monero

> Monero is a secure, private, untraceable currency. It is open-source and freely available to all.

For more information and questions about Monero,
one can go to [getmonero.org](https://getmonero.org) and
[r/Monero](https://www.reddit.com/r/Monero), respectively.
