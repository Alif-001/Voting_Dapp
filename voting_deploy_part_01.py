import json
from web3 import Web3
from solcx import compile_standard, install_solc

# install_solc("0.8.0")

with open("./Election.sol", "r") as file:
    election_list_file = file.read()

# Solidity source code
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"Election.sol": {"content": election_list_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.8.0",
)

with open("compiled_code_election.json", "w") as file:
    json.dump(compiled_sol, file)

# get bytecode
bytecode = compiled_sol["contracts"]["Election.sol"]["Election"]["evm"]["bytecode"]["object"]

# get abi
abi = json.loads(compiled_sol["contracts"]["Election.sol"]["Election"]["metadata"])["output"]["abi"]


# For connecting to ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
chain_id = 1337

# this is the ganache-cli public and private key
my_address = "0xd22A6FC3C2aDf51eE5c774Ec8413317E74FeCf30"
private_key = "0x79ff4f45473ed8c3ab79ffd43856d2da218ade59310a1326223eb49986507cad"
