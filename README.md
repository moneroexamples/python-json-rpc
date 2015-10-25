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

**Basic example showing how to get current balance**
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

**Basic example showing how to get a block header**
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

**Basic example showing how to get a mining status**
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

More examples are comming soon.

# What is Monero

> Monero is a secure, private, untraceable currency. It is open-source and freely available to all.

For more information and questions about Monero,
one can go to [getmonero.org](https://getmonero.org) and
[r/Monero](https://www.reddit.com/r/Monero), respectively.
