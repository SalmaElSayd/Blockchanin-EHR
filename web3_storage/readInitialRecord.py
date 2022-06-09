from solcx import compile_standard
from web3 import Web3
import hashRecordTracker
import json
import solcx
import os
import csv
import rsa
from dotenv import load_dotenv
from ast import literal_eval
load_dotenv()
solcx.install_solc('0.8.0')

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


# Function that prints the patient record in a readable way
def print_init_record(rec_list):
    gender = 'Female'
    if(rec_list[5]):
        gender = 'Male'
    return 'Id: ' + str(rec_list[0]) + '\n' + \
        'Name: ' + rec_list[1] + '\n' + \
        'Age: ' + str(rec_list[2]) + '\n' + \
        'Weight: ' + str(rec_list[3]) + '\n' + \
        'Height: ' + str(rec_list[4]) + '\n' + \
        'Gender: ' + gender + '\n' + \
        'Blood Pressure: ' + str(rec_list[6]) + '\n' + \
        'Blood Glucose: ' + str(rec_list[7]) + '\n' + \
        'Pulse: ' + str(rec_list[8]) + '\n' + \
        'Oxygen Level: ' + str(rec_list[9])


# bytecode initial record
initial_record_bytecode = compiled_sol["contracts"]["InitialRecord.sol"]["InitialRecord"]["evm"]["bytecode"]["object"]
# abi initial record
initial_record_abi = compiled_sol["contracts"]["InitialRecord.sol"]["InitialRecord"]["abi"]

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337
my_address = "0x4b4ADE8a7d63ae6710cb5b05782385357694f1A0"
private_key = os.getenv("PRIVATE_KEY")

# Getting the patient Id as input
patient_id = int(input('Enter Patient ID: '))

# Getting the patient info
try:
    curr_record_hash = hashRecordTracker.get_patient_hash(patient_id)['hash']
except:
    print("Patient Id does not exist")
else:
    # Getting the latest transaction by the latest block
    curr_block = w3.eth.get_block('latest')
    # print(block)
    zero_byte = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    parent_hash = curr_block["parentHash"]
    # Iterating through the blocks
    while(not(parent_hash) == zero_byte):

        all_transactions = curr_block['transactions']

        transaction_receipt = w3.eth.get_transaction_receipt(
            all_transactions[0])

        InitialRecordContract = w3.eth.contract(
            abi=initial_record_abi, address=transaction_receipt.contractAddress)

        # Reading the latest initial record
        enc_rec = InitialRecordContract.functions.readRecord().call()
        print(enc_rec)
        # Decrypting the record using the private key
        dr_private_key = rsa.PrivateKey(int(os.getenv("N")), int(os.getenv(
            "E")), int(os.getenv("D")), int(os.getenv("P")), int(os.getenv("Q")))
        rec = rsa.decrypt(enc_rec[0], dr_private_key)

        # Decoding the bytes into string and print the record in a readable way
        rec_string = rec.decode("utf-8")
        rec_details = rec_string.split(',')
        # Checking if it is an initial record for a patient and it has the patient id to print it
        if(len(rec_details) == 10 and rec_details[0] == patient_id):
            print(print_init_record(rec_details))

        # Getting the previos block through the hash of the previous block
        curr_block = w3.eth.get_block(parent_hash)
        parent_hash = curr_block["parentHash"]