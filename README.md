# Examples of json-rpc calls for Monero's simplewallet.

The simplewallet RPC docs are here:
https://getmonero.org/knowledge-base/developer-guides/wallet-rpc

The examples demonstrate how to call the most popular procedures
that simplewallet exposes for other applications to use such as:

 - getbalance
 - query_key
 - get_payments
 - getaddress
 - incoming_transfers
 - transfer
 
 
Using these procedures, other applications can be developed
on top of the simplewallet. For example, a GUI,
or an web applications allowing for accessing wallet balance
 online.

# Prerequisites

Before executing this code make sure that simplewallet is
running and listening for the incoming rpc calls.

For example, you can run the simplewallet in rpc mode as follows:
```
/opt/bitmonero/simplewallet --wallet-file ~/wallet.bin --password <wallet_password> --rpc-bind-port 18082
```

The code was written, tested and executed on Ubuntu 15.10 with
Python 3.4.3 and requires the [Requests package](https://pypi.python.org/pypi/requests).

# What is Monero

> Monero is a secure, private, untraceable currency. It is open-source and freely available to all.

More can be found at [getmonero.org](https://getmonero.org)