import hashRecordTracker
import json
import solcx
import os
import csv
import rsa
from dotenv import load_dotenv
load_dotenv()
from web3 import Web3
solcx.install_solc('0.8.0') 
from solcx import compile_standard
# print(hashRecordTracker.set_patient_hash(3,"xcv"))

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

# bytecode initial record
initial_record_bytecode = compiled_sol["contracts"]["InitialRecord.sol"]["InitialRecord"]["evm"]["bytecode"]["object"]
# abi initial record
initial_record_abi = compiled_sol["contracts"]["InitialRecord.sol"]["InitialRecord"]["abi"]

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337
my_address = "0x9d5A2f02E11793A196209e8055382b0895e1CE0A"
private_key = os.getenv("PRIVATE_KEY")

# trnxn = w3.eth.getTransaction('0x115f2b60cac1a2ae05e2a868f6f5b966b86342224f22ccbaf12476d4ce3d0473')
trnxn_receipt = w3.eth.getTransactionReceipt('0x9bee7f10a6292a2a4d539a9201043a030cdb9b3af8b0cf44dca9b9772febf4a9')
InitialRecordContract = w3.eth.contract(abi=initial_record_abi, address=trnxn_receipt.contractAddress)
print(InitialRecordContract.functions.readRecord().call())
# print(trnxn.input)
# print(InitialRecordContract.decode_function_input(trnxn.input))
# InitialRecordContract.decode_function_input(trnxn.input)
# print(trnxn_input)

(bob_pub, bob_priv) = rsa.newkeys(512)
msg = (2, 1, 1, 1, 1, 1, 1, 1)
converted_msg = int.from_bytes(msg, byteorder ='big')
print(converted_msg)
# crypto = rsa.encrypt(msg, bob_pub)
# print(crypto)