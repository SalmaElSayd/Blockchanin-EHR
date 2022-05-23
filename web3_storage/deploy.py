import json
import solcx
import os
from dotenv import load_dotenv
load_dotenv()
from web3 import Web3
solcx.install_solc('0.8.0') 
from solcx import compile_standard

# start to deploy InitialRecord.sol
with open("./InitialRecord.sol", "r") as file:
    initial_record_file =file.read()    

compiled_sol = compile_standard(
    {"language" : "Solidity",
    "sources":{"InitialRecord.sol":{"content":initial_record_file}},
    "settings":{
        "outputSelection":{
            "*":{"*":["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
        }
    },
    },
    solc_version = "0.8.0",

)
with open("compiled_initial_record.json", "w") as file:
    json.dump(compiled_sol,file)

# bytecode initial record
initial_record_bytecode = compiled_sol["contracts"]["InitialRecord.sol"]["InitialRecord"]["evm"]["bytecode"]["object"]
# abi initial record
initial_record_abi = compiled_sol["contracts"]["InitialRecord.sol"]["InitialRecord"]["abi"]

# connect to blockchain ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337
my_address = "0x59436001ccBB17844fb38F9290895339f3536e43"
private_key = os.getenv("PRIVATE_KEY")

# create the contract for initial record
InitialRecord = w3.eth.contract(abi=initial_record_abi, bytecode=initial_record_bytecode)

# Build, Sign, Send the transaction
nonce = w3.eth.getTransactionCount(my_address)
initial_record_transaction = InitialRecord.constructor().buildTransaction({
    "gasPrice": w3.eth.gas_price, "chainId": chain_id, "from": my_address, "nonce": nonce
})
signed_initial_record_trnxn = w3.eth.account.sign_transaction(initial_record_transaction, private_key=private_key)
hashed_initial_record_trnxn = w3.eth.send_raw_transaction(signed_initial_record_trnxn.rawTransaction)
initial_record_trnxn_receipt = w3.eth.wait_for_transaction_receipt(hashed_initial_record_trnxn)

# Work with the initial record contract
# we need Contract Address, Contract ABI
initial_record = w3.eth.contract(address=initial_record_trnxn_receipt.contractAddress, abi=initial_record_abi)



# start to deploy VisitRecord.sol
with open("./VisitRecord.sol", "r") as file:
    visit_record_file =file.read()

compiled_sol_v = compile_standard(
    {"language" : "Solidity",
    "sources":{"VisitRecord.sol":{"content":visit_record_file}},
    "settings":{
        "outputSelection":{
            "*":{"*":["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
        }
    },
    },
    solc_version = "0.8.0",

)



with open("compiled_visit_record.json", "w") as file:
    json.dump(compiled_sol_v,file)


# bytecode visit record
visit_record_bytecode = compiled_sol_v["contracts"]["VisitRecord.sol"]["VisitRecord"]["evm"]["bytecode"]["object"]
# abi visit record
visit_record_abi = compiled_sol_v["contracts"]["VisitRecord.sol"]["VisitRecord"]["abi"]

# create the contract for visit record
VisitRecord = w3.eth.contract(abi=visit_record_abi, bytecode=visit_record_bytecode)

# Build, Sign, Send the transaction
nonce = w3.eth.getTransactionCount(my_address)
visit_record_transaction = VisitRecord.constructor().buildTransaction({
    "gasPrice": w3.eth.gas_price, "chainId": chain_id, "from": my_address, "nonce": nonce
})
signed_visit_record_trnxn = w3.eth.account.sign_transaction(visit_record_transaction, private_key=private_key)
hashed_visit_record_trnxn = w3.eth.send_raw_transaction(signed_visit_record_trnxn.rawTransaction)
visit_record_trnxn_receipt = w3.eth.wait_for_transaction_receipt(hashed_visit_record_trnxn)

# Work with the visit record contract
# we need Contract Address, Contract ABI
visit_record = w3.eth.contract(address=visit_record_trnxn_receipt.contractAddress, abi=visit_record_abi)
print(visit_record.functions.readRecord().call())

