from solcx import compile_standard
from web3 import Web3
import hashRecordTracker
import json
import solcx
import os
import csv
import rsa
from dotenv import load_dotenv
load_dotenv()
solcx.install_solc('0.8.0')
# print(hashRecordTracker.set_patient_hash(3,"xcv"))

with open("./InitialRecord.sol", "r") as file:
    initial_record_file = file.read()

compiled_sol = compile_standard(
    {"language": "Solidity",
     "sources": {"InitialRecord.sol": {"content": initial_record_file}},
     "settings": {
         "outputSelection": {
             "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
         }
     },
     },
    solc_version="0.8.0",

)

# bytecode initial record
initial_record_bytecode = compiled_sol["contracts"]["InitialRecord.sol"]["InitialRecord"]["evm"]["bytecode"]["object"]
# abi initial record
initial_record_abi = compiled_sol["contracts"]["InitialRecord.sol"]["InitialRecord"]["abi"]

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337
my_address = "0x4b4ADE8a7d63ae6710cb5b05782385357694f1A0"
private_key = os.getenv("PRIVATE_KEY")

# trnxn = w3.eth.getTransaction('0x115f2b60cac1a2ae05e2a868f6f5b966b86342224f22ccbaf12476d4ce3d0473')
trnxn_receipt = w3.eth.getTransactionReceipt(
    '0x533d6cc6f746beefa08d9b578e634e13dff0e151bace1517124dc9f1f2538927')
InitialRecordContract = w3.eth.contract(
    abi=initial_record_abi, address=trnxn_receipt.contractAddress)
# print(InitialRecordContract.functions.readRecord().call())
# print(trnxn.input)
# print(InitialRecordContract.decode_function_input(trnxn.input))
# InitialRecordContract.decode_function_input(trnxn.input)
# print(trnxn_input)

# rec = InitialRecordContract.functions.readRecord().call()

# print('Encrypted Patient Record: ')
# print(type(rec[0]))

# print('Encryption Process ...')

# dr_priv = rsa.PrivateKey(10509342123090674585209035091359267482091408553303762051145163142506185871998812777851109828523977656519777131668087789862151876294575731215149784463254067, 65537,
#  7310693308996503568055905973954697415330993422724850266440453296105360538025099995033852898088488802317161950317168521156549133634732177901754187968200273, 7104077563067677004513110177694313288983504745114742218709049219128633950306208487, 1479339439890988324680698702567533837223023595488148956851875250325680341)

# Converted Patient:
# b'3,omar,58,42,61,True,21,52,4,6'
# Encrypted Patient:
# b"]\xf8S.;\xfaI\xde\x12\x9f\x02x\x9a\x812d`\xa0\xff\x8d\x11\x8cC\xbbyDT\xe1\xe9`\x17'\x1al/\xe4\x13\xabLp\xdc`k`g^E\x85\x8e9d4W'\xf1\x13\x08\x89w\x91\x8b\xc3\xcd\xa4"

# msg = (2, 1, 1, 1, 1, 1, 1, 1)
# converted_rec = bytes.from_bytes(rec, byteorder='big')
# print(converted_rec)

# crypto = rsa.decrypt(rec[0], dr_priv)
# print('Encrypted Patient: ')
# print(crypto)

# print(dr_pub)
# print(dr_priv)

transaction_receipt = w3.eth.getTransactionReceipt()
