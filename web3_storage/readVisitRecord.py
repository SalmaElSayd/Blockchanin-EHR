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

with open("./VisitRecord.sol", "r") as file:
    visit_record_file = file.read()

compiled_sol_v = compile_standard(
    {"language": "Solidity",
     "sources": {"VisitRecord.sol": {"content": visit_record_file}},
     "settings": {
         "outputSelection": {
             "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
         }
     },
     },
    solc_version="0.8.0",

)


# Function that prints the visit record in a readable way
def print_visit_record(rec_list):
    return 'Age: ' + str(rec_list[1]) + '\n' + \
        'Weight: ' + str(rec_list[2]) + '\n' + \
        'Height: ' + str(rec_list[3]) + '\n' + \
        'Reason of visit: ' + rec_list[4] + '\n' + \
        'Diagnosis: ' + rec_list[5] + '\n' + \
        'Referrals: ' + rec_list[6] + '\n' + \
        'Follow-up: ' + rec_list[7] + '\n' + \
        'Lab tests: ' + rec_list[8] + '\n' + \
        'Blood Pressure: ' + str(rec_list[9]) + '\n' + \
        'Blood Glucose: ' + str(rec_list[10]) + '\n' + \
        'Pulse: ' + str(rec_list[11]) + '\n' + \
        'Oxygen Level: ' + str(rec_list[12])


# bytecode visit record
visit_record_bytecode = compiled_sol_v["contracts"]["VisitRecord.sol"]["VisitRecord"]["evm"]["bytecode"]["object"]
# abi visit record
visit_record_abi = compiled_sol_v["contracts"]["VisitRecord.sol"]["VisitRecord"]["abi"]

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337
my_address = "0x4b4ADE8a7d63ae6710cb5b05782385357694f1A0"
private_key = os.getenv("PRIVATE_KEY")

# Getting the patient Id as input
patient_id = eval(input('Enter Patient ID: '))

# Getting the visit info
try:
    curr_record_hash = hashRecordTracker.get_patient_hash(patient_id)['hash']
except:
    print("Patient Id does not exist")
else:
    while(curr_record_hash != ''):
        # Getting the transaction by the latest block
        transaction_receipt = w3.eth.get_transaction_receipt(
            curr_record_hash)

        VisitRecordContract = w3.eth.contract(
            abi=visit_record_abi, address=transaction_receipt.contractAddress)

        try:
            # Reading the latest visit record
            enc_rec = VisitRecordContract.functions.readRecord().call()
        except:
            break

        # Decrypting the record using the private key
        dr_private_key = rsa.PrivateKey(int(os.getenv("N")), int(os.getenv(
            "E")), int(os.getenv("D")), int(os.getenv("P")), int(os.getenv("Q")))
        rec = rsa.decrypt(enc_rec[0], dr_private_key)

        # Decoding the bytes into string and print the record in a readable way
        rec_string = rec.decode("utf-8")
        rec_details = rec_string.split(',')
        print(print_visit_record(rec_details))

        # updating the hash to get the previous visit
        curr_record_hash = enc_rec[1]
