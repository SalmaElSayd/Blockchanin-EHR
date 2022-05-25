import json
# from matplotlib.font_manager import _Weight
import currentIdCounter
import solcx
import os
import csv
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
my_address = "0x9d5A2f02E11793A196209e8055382b0895e1CE0A"
private_key = os.getenv("PRIVATE_KEY")

# create the contract for initial record
InitialRecord = w3.eth.contract(abi=initial_record_abi, bytecode=initial_record_bytecode)


#getting inputs
patientId = int(currentIdCounter.get_current_id())
name = str(input("enter name: "))
age = int(input("enter age: "))
weight = int(input("enter weight: "))
height = int(input("height: "))
female = bool(input("female?: "))
blood_pressure = int(input("blood pressure: "))
blood_glucose = int(input("blood glucose: "))
pulse = int(input("pulse: "))
oxygen_level = int(input("oxygen level: "))



# Build, Sign, Send the transaction
nonce = w3.eth.getTransactionCount(my_address)
initial_record_transaction = InitialRecord.constructor(patientId,name,age,weight,height,female,blood_pressure,blood_glucose,pulse,oxygen_level).buildTransaction({
    "gasPrice": w3.eth.gas_price, "chainId": chain_id, "from": my_address, "nonce": nonce
})
signed_initial_record_trnxn = w3.eth.account.sign_transaction(initial_record_transaction, private_key=private_key)
hashed_initial_record_trnxn = w3.eth.send_raw_transaction(signed_initial_record_trnxn.rawTransaction)
initial_record_trnxn_receipt = w3.eth.wait_for_transaction_receipt(hashed_initial_record_trnxn)
print("INITIAL.....")
print(initial_record_trnxn_receipt)
print(initial_record_abi)

# Work with the initial record contract
# we need Contract Address, Contract ABI
initial_record = w3.eth.contract(address=initial_record_trnxn_receipt.contractAddress, abi=initial_record_abi)
# print(initial_record_abi)
currentIdCounter.increment_current_id()
