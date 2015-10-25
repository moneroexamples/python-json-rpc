# Basic example of json-rpc calls to Monero's bitmonerod.
#
# The example gets a header of a block with
# the following hash:
# d78e2d024532d8d8f9c777e2572623fd0f229d72d9c9c9da3e7cb841a3cb73c6
#
# The bitmonerod RPC docs are here: not avaliable


import requests
import json

def main():

    # bitmonerod is running on the localhost and port of 18082
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

    # pretty print json outout
    print(json.dumps(response.json(), indent=4))

if __name__ == "__main__":
    main()