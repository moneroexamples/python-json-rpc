# Basic example of json-rpc calls to Monero's bitmonerod.
#
# The example gets a header a mining status
#
# The bitmonerod RPC docs are here: not avaliable


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