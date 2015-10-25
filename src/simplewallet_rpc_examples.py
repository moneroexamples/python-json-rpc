# Examples of json-rpc calls for Monero's simplewallet.
#
# The simplewallet RPC docs are here:
# https://getmonero.org/knowledge-base/developer-guides/wallet-rpc
#
# The examples demonstrate how to call the most popular procedures
# that simplewallet exposes for other applications to use.
#
# Using these procedures, other applications can be developed
# on that ese monero's simplewallet. For example, a GUI,
# or an web applications allowing for accessing wallets online.
#
# Before executing this code make sure that simplewallet is
# running and listening for the incoming rpc calls.
#
# For example, you can run the simplewallet in rpc mode as follows:
# /opt/bitmonero/simplewallet --wallet-file ~/wallet.bin --password <wallet_password> --rpc-bind-port 18082
#
#
# The code was written, tested and executed on Ubuntu 15.10 with
# Python 3.4.3. It uses Requests package (https://pypi.python.org/pypi/requests).
#
#
# Example output:
#
# get_balance():
# return the wallet's balance
# {'jsonrpc': '2.0', 'id': '0', 'result': {'unlocked_balance': 4800000000000, 'balance': 4800000000000}}
#
# get_address():
# return the wallet's address
# {'jsonrpc': '2.0', 'id': '0', 'result': {'address': '48daf1rG3hE1Txapcsxh6WXNe9MLNKtu7W7tKTivtSoVLHErYzvdcpea2nSTgGkz66RFP4GKVAsTV14v6G3oddBTHfxP6tU'}}
#
# get_view_key():
# return the wallet's the view key
# {'jsonrpc': '2.0', 'id': '0', 'result': {'key': '1ddabaa51cea5f6d9068728dc08c7ffaefe39a7a4b5f39fa8a976ecbe2cb520a'}}
#
# get_mnemonic_key():
# return the wallet's mnemonic key
# {'jsonrpc': '2.0', 'error': {'code': 0, 'message': 'The wallet is non-deterministic. Cannot display seed.'}, 'id': '0'}
#
# get_payments():
# get a list of incoming payments using a given payment id
# {'jsonrpc': '2.0', 'id': '0', 'result': {'payments': [{'amount': 4800000000000, 'payment_id': '426870cb29c598e191184fa87003ca562d9e25f761ee9e520a888aec95195912', 'unlock_time': 0, 'tx_hash': '66040ad29f0d780b4d47641a67f410c28cce575b5324c43b784bb376f4e30577', 'block_height': 795523}]}}
#
# incoming_transfers():
# return a list of incoming transfers to the wallet
# {'jsonrpc': '2.0', 'id': '0', 'result': {'transfers': [{'global_index': 346865, 'amount': 800000000000, 'tx_hash': '<66040ad29f0d780b4d47641a67f410c28cce575b5324c43b784bb376f4e30577>', 'tx_size': 521, 'spent': False}, {'global_index': 177947, 'amount': 4000000000000, 'tx_hash': '<66040ad29f0d780b4d47641a67f410c28cce575b5324c43b784bb376f4e30577>', 'tx_size': 521, 'spent': False}]}}
#
# transfer():
# send monero to a number of recipients
#
# Transfer 1 xmr to:  489MAxaT7xXP3Etjk2suJT1uDYZU6cqFycsau2ynCTBacncWVEwe9eYFrAD6BqTn4Y2KMs7maX75iX1UFwnJNG5G88wxKoj
# {'id': '0', 'jsonrpc': '2.0', 'result': {'tx_key': '', 'tx_hash': '<e8409a93edeed9f6c67e6716bb180d9593e8beafa63d51facf68bee233bf694d>'}}
#
#
# Last update: 25 Oct 2015

import requests
import json


class SimplewalletRpcExamples():

    def __init__(self):
        # simple wallet is running on the localhost and port of 18082
        self.url = "http://localhost:18082/json_rpc"

        # standard json header
        self.headers = {'content-type': 'application/json'}

    def get_balance(self):
        """return the wallet's balance"""

        rpc_input = {
            "method": "getbalance"
        }

        response = self.__do_rpc(rpc_input)

        return response.json()

    def get_view_key(self):
        """return the wallet's the view key"""

        rpc_input = {
            "method": "query_key",
            "params": {"key_type": "view_key"}
        }

        response = self.__do_rpc(rpc_input)

        return response.json()

    def get_mnemonic_key(self):
        """return the wallet's mnemonic key"""

        rpc_input = {
            "method": "query_key",
            "params": {"key_type": "mnemonic"}
        }

        response = self.__do_rpc(rpc_input)

        return response.json()

    def get_address(self):
        """return the wallet's address"""

        rpc_input = {
            "method": "getaddress"
        }

        response = self.__do_rpc(rpc_input)

        return response.json()

    def get_payments(self):
        """get a list of incoming payments using a given payment id"""

        # en example of a payment id
        payment_id = "426870cb29c598e191184fa87003ca562d9e25f761ee9e520a888aec95195912"

        rpc_input = {
            "method": "get_payments",
            "params": {"payment_id": payment_id}
        }

        response = self.__do_rpc(rpc_input)

        return response.json()

    def incoming_transfers(self):
        """return a list of incoming transfers to the wallet"""

        rpc_input = {
            "method": "incoming_transfers",
            "params": {"transfer_type": "all"}
        }

        response = self.__do_rpc(rpc_input)

        return response.json()

    def transfer(self):
        """send monero to a number of recipients

        DON'T RUN THIS FUNCTION without changing
        the recipient address! The reason is that it will
        send 1 xmr to my address.

        For this reason, this method is not executed
        by self.execute()
        """

        print("transfer():\n send monero to a number of recipients\n")

        destination_address = "489MAxaT7xXP3Etjk2suJT1uDYZU6cqFycsau2ynCTBacncWVEwe9eYFrAD6BqTn4Y2KMs7maX75iX1UFwnJNG5G88wxKoj"

        # send 1 xmr to the given destination_address
        recipents = [
            {"address": destination_address, "amount": 1}
        ]

        mixin = 4

        rpc_input = {
            "method": "transfer",
            "params": {"destinations": recipents, "mixin": mixin}
        }

        print("Transfer 1 xmr to: ", destination_address)

        response = self.__do_rpc(rpc_input)

        print(response.json(), "\n")

        return response.json()



    def execute(self):
        """run read-only examples"""

        example_functions = [self.get_balance,
                             self.get_address,
                             self.get_view_key,
                             self.get_mnemonic_key,
                             self.get_payments,
                             self.incoming_transfers]

        for fun_obj in example_functions:
            print(fun_obj.__name__ + "():\n" + fun_obj.__doc__)
            json_result = fun_obj()
            print(json_result, "\n")

    def __do_rpc(self, rpc_input):
        """does the rpc calls"""

        # add standard rpc values
        rpc_input.update({"jsonrpc": "2.0", "id": "0"})

        # execute the rpc requrest
        response = requests.post(
            self.url,
            data=json.dumps(rpc_input),
            headers=self.headers)

        return response


if __name__ == "__main__":
    sw = SimplewalletRpcExamples()
    sw.execute()
    #sw.transfer() #<-- DONT run without modifying destination_address

