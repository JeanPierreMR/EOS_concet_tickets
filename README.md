# EOS_concet_tickets
Concert tickets app using an EOS blockchain

# How to run Nodeos

If you have nodeos source install just run the command to run EOS

nodeos -e -p eosio --plugin eosio::producer_plugin --plugin eosio::producer_api_plugin --plugin eosio::chain_api_plugin --plugin eosio::http_plugin --plugin eosio::history_plugin --plugin eosio::history_api_plugin --filter-on="*" --access-control-allow-origin='*' --max-transaction-time=1000 --contracts-console --http-validate-host=false --verbose-http-errors >> nodeos.log 2>&1 &

#compile the contract

In this repository there are two files eosio.nft.cpp and eos.io.hpp, run the following command in CLI while in the folder


1. eosio-cpp -o eosio.nft.wasm eosio.nft.cpp --abigen --contract nft


that should create two new files: eosio.nft.abi and eosio.nft.wasm

Now we are ready to run the contract!



# How to execute de Contract in a clean NODEOS

1. cleos wallet create --name local --to-console

NOTE: save the password to unlock the wallet in the future

2. cleos create key --to-console

3. cleos create account eosio nft pubkey

Note: pubkey has to be replaced with the publickey output in command 2

4. cleos wallet import --name local --private-key privatekey

Note: privatekey has to be replaced with the privatekey output in command 2


5. cleos set contract nft ./ eosio.nft.wasm eosio.nft.abi -p nft@active


Great! now the command should be working







