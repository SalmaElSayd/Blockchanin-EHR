import json
import solcx
import hashRecordTracker
import os
import csv
from dotenv import load_dotenv
load_dotenv()
from web3 import Web3
solcx.install_solc('0.8.0') 
from solcx import compile_standard

class visit_record:
    def __init__(self,patientId,age,weight,height,reason,diagnosis,referrals,follow_up,lab_tests,blood_pressure,blood_glucose,pulse,oxygen_level ):
        self.patientId = patientId
        self.age = age
        self.weight = weight
        self.height = height
        self.reason = reason
        self.diagnosis = diagnosis
        self.referrals = referrals
        self.follow_up = follow_up
        self.lab_tests = lab_tests
        self.blood_pressure = blood_pressure
        self.blood_glucose = blood_glucose
        self.pulse = pulse
        self.oxygen_level = oxygen_level

    def to_string(self):
        return (str(self.patientId)+"," + 
        str(self.age)+"," +
        str(self.weight)+"," +
        str(self.height)+"," +
        str(self.reason)+"," +
        str(self.diagnosis)+"," +
        str(self.referrals)+"," +
        str(self.follow_up)+"," +
        str(self.lab_tests)+"," +
        str(self.blood_pressure)+"," +
        str(self.blood_glucose)+"," +
        str(self.pulse)+"," +
        str(self.oxygen_level))

    def to_byte(self):
        return bytes(self.to_string(),"UTF-8") 
    
    def string2obj(self, data):
        patientId,age,weight,height,reason,diagnosis,referrals,follow_up,lab_tests,blood_pressure,blood_glucose,pulse,oxygen_level = data.split(",")
        self.patientId = patientId
        self.age = age
        self.weight = weight
        self.height = height
        self.reason = reason
        self.diagnosis = diagnosis
        self.referrals = referrals
        self.follow_up = follow_up
        self.lab_tests = lab_tests
        self.blood_pressure = blood_pressure
        self.blood_glucose = blood_glucose
        self.pulse = pulse
        self.oxygen_level = oxygen_level





# connect to blockchain ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337
my_address = "0x9d5A2f02E11793A196209e8055382b0895e1CE0A"
private_key = os.getenv("PRIVATE_KEY")

patientId = int(input("enter patient id: "))
age = int(input("enter age: "))
weight = int(input("enter weight: "))
height = int(input("height: "))

reason = str(input("enter reason of visit: "))
diagnosis = str(input("enter diagnosis: "))
referrals = str(input("enter referrals: "))
follow_up = str(input("enter follow-up: "))
lab_tests = str(input("enter lab tests: "))

blood_pressure = int(input("blood pressure: "))
blood_glucose = int(input("blood glucose: "))
pulse = int(input("pulse: "))
oxygen_level = int(input("oxygen level: "))

previous_record_hash =hashRecordTracker.get_patient_hash(patientId)

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

visit = visit_record(patientId, age, weight, height, reason, diagnosis, referrals, follow_up, lab_tests, blood_pressure, blood_glucose, pulse, oxygen_level)
# Build, Sign, Send the transaction
nonce = w3.eth.getTransactionCount(my_address)
visit_record_transaction = VisitRecord.constructor(visit.to_byte(), previous_record_hash['hash']).buildTransaction({
    "gasPrice": w3.eth.gas_price, "chainId": chain_id, "from": my_address, "nonce": nonce
})
signed_visit_record_trnxn = w3.eth.account.sign_transaction(visit_record_transaction, private_key=private_key)
hashed_visit_record_trnxn = w3.eth.send_raw_transaction(signed_visit_record_trnxn.rawTransaction)
visit_record_trnxn_receipt = w3.eth.wait_for_transaction_receipt(hashed_visit_record_trnxn)
print("VISIT.....")
print(visit_record_trnxn_receipt)
print("hash.....")
print(visit_record_trnxn_receipt['transactionHash'].hex())
hash = visit_record_trnxn_receipt['transactionHash'].hex()

# # Work with the visit record contract
# # we need Contract Address, Contract ABI
visit_record = w3.eth.contract(address=visit_record_trnxn_receipt.contractAddress, abi=visit_record_abi)
print(visit_record.functions.readRecord().call())

hashRecordTracker.set_patient_hash(int(patientId),hash)
