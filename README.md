# Examples of json-rpc calls to bitmonero.

## simplewallet
The examples demonstrate how to call the most popular procedures
that simplewallet exposes for other applications to use such as:

 - getbalance
 - query_key
 - get_payments
 - getaddress
 - incoming_transfers
 - transfer

The documentaion of the procedures can be found 
[here](https://getmonero.org/knowledge-base/developer-guides/wallet-rpc).
 
Using these procedures, other applications can be developed
on top of the simplewallet. For example, a GUI,
or an web applications allowing for accessing wallet balance
 online.


### Prerequisites

Before executing this code make sure that simplewallet is
running and listening for the incoming rpc calls.

For example, you can run the simplewallet in rpc mode as follows:
```
/opt/bitmonero/simplewallet --wallet-file ~/wallet.bin --password <wallet_password> --rpc-bind-port 18082
```

The code was written, tested and executed on Ubuntu 15.10 with
Python 3.4.3 and requires the [Requests package](https://pypi.python.org/pypi/requests).

 
## bitmonreod

Coming as soon as I will figure out the rpc calls for the bitmonreod. 
There is no documentation for the procedures in bitmonreod.

# What is Monero

> Monero is a secure, private, untraceable currency. It is open-source and freely available to all.

More can be found at [getmonero.org](https://getmonero.org)