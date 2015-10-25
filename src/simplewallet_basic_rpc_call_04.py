# Basic example of json-rpc calls to Monero's simplewallet.
#
# Transfer 1 xmr to some address
#
# The simplewallet RPC docs are here:
# https://getmonero.org/knowledge-base/developer-guides/wallet-rpc
#
# The bitmonerod RPC docs are here: not avaliable


import requests
import json

def main():
    """DONT RUN IT without changing the destination address!!!"""

    # simple wallet is running on the localhost and port of 18082
    url = "http://localhost:18082/json_rpc"

    # standard json header
    headers = {'content-type': 'application/json'}

    destination_address = "489MAxaT7xXP3Etjk2suJT1uDYZU6cqFycsau2ynCTBacncWVEwe9eYFrAD6BqTn4Y2KMs7maX75iX1UFwnJNG5G88wxKoj"

    # send 1 xmr to the given destination_address
    recipents = [
        {"address": destination_address, "amount": 1}
    ]

    # using given mixin
    mixin = 4

    # simplewallet' procedure/method to call
    rpc_input = {
        "method": "transfer",
        "params": {"destinations": recipents, "mixin": mixin}
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