# Basic example of json-rpc calls to Monero's bitmonerod.
#
# The example gets full block info
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
           "method": "getblock",
           "params": {"hash": block_hash}
    }

    # add standard rpc values
    rpc_input.update({"jsonrpc": "2.0", "id": "0"})

    # execute the rpc request
    response = requests.post(
        url,
        data=json.dumps(rpc_input),
        headers=headers)

    # the response will contain binary blob. For some reason
    # python's json encoder will crash trying to parse such
    # response. Thus, its better to remove it from the response.
    response_json_clean = json.loads(
                            "\n".join(filter(
                                lambda l: "blob" not in l, response.text.split("\n")
                            )))

    # pretty print json output
    print(json.dumps(response_json_clean, indent=4))

if __name__ == "__main__":
    main()