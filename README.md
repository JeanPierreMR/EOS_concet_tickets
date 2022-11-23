# EOS_concet_tickets
Concert tickets app using an EOS blockchain

# How to run Nodeos

If you have nodeos source installed just run the command to run EOS

nodeos -e -p eosio --plugin eosio::producer_plugin --plugin eosio::producer_api_plugin --plugin eosio::chain_api_plugin --plugin eosio::http_plugin --plugin eosio::history_plugin --plugin eosio::history_api_plugin --filter-on="*" --access-control-allow-origin='*' --max-transaction-time=1000 --contracts-console --http-validate-host=false --verbose-http-errors >> nodeos.log 2>&1 &

# Compile the contract

In this repository there are two files eosio.nft.cpp and eos.io.hpp, run the following command in CLI while in the folder


1. eosio-cpp -o eosio.nft.wasm eosio.nft.cpp --abigen --contract nft


that should create two new files: eosio.nft.abi and eosio.nft.wasm

Now we are ready to run the contract!

NOTE: if you dont have eosio-cpp you can find it here: https://developers.eos.io/welcome/latest/getting-started-guide/local-development-environment/installing-eosiocdt



# How to execute de Contract in a clean NODEOS

1. cleos wallet create --name local --to-console

NOTE: save the password to unlock the wallet in the future

1.1 cleos wallet import --name local 5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3
NOTE: run this command as is

2. cleos create key --to-console

3. cleos create account eosio nft pubkey

Note: pubkey has to be replaced with the publickey output in command 2

4. cleos wallet import --name local --private-key privatekey

Note: privatekey has to be replaced with the privatekey output in command 2


5. cleos set contract nft ./ eosio.nft.wasm eosio.nft.abi -p nft@active


Great! now the contract is in the EOS blockchain

# How to run the WEB APP

to do this the requirements are:
  - python 3 installed
  - flask installed

Now run the command:

1. python3 main.py

Note: the command should be run while being in the folder where main.py is located

now the WEB APP and contract is up, now go to your browser and search localhost:3023/ and try it out!


# TEAM MEMBERS

- Anesveth Maatens
- David Corzo
- Katherine Garcia
- Jean Pierre Mejicanos
- ian Jenatz
- Fabricio Juarez
- Adriana Mundo
- Andrea Reyes
- Pablo Velasquez







