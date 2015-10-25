# Basic example of json-rpc calls to Monero's simplewallet.
#
# The example gets payment information based on given
# payment id: 426870cb29c598e191184fa87003ca562d9e25f761ee9e520a888aec95195912
#
# The simplewallet RPC docs are here:
# https://getmonero.org/knowledge-base/developer-guides/wallet-rpc
#

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