# Basic example of json-rpc calls to Monero's bitmonerod.
#
# The example gets blockchain information
#
# The bitmonerod RPC docs are here: not avaliable


import requests
import json

def main():

    # bitmonerod is running on the localhost and port of 18082
    url = "http://localhost:18081/json_rpc"

    # standard json header
    headers = {'content-type': 'application/json'}

    # bitmonerod' procedure/method to call
    rpc_input = {
           "method": "get_info"
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