# Basic example of json-rpc calls to Monero's simplewallet.
#
# The example gets the wallet's balance
#
# The simplewallet RPC docs are here:
# https://getmonero.org/knowledge-base/developer-guides/wallet-rpc
#
#

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