import rsa
from solcx import compile_standard
from web3 import Web3
import json
import solcx
import hashRecordTracker
import os
import csv
from dotenv import load_dotenv
import verify_dr
load_dotenv()
from Visit_Record import visit_record
solcx.install_solc('0.8.0')
def __main__(dr_email, dr_pass,patientId, age, weight, height, reason, diagnosis, referrals, follow_up, lab_tests, blood_pressure, blood_glucose, pulse, oxygen_level,lab_test_results):

    # connect to blockchain ganache
    w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
    chain_id = 1337
    my_address =os.getenv("ADDRESS")
    private_key = os.getenv("PRIVATE_KEY")

    patientId = str(patientId)
    age = int(age)
    weight = int(weight)
    height = int(height)

    reason = str(reason)
    diagnosis = str(diagnosis)
    referrals = str(referrals)
    follow_up = str(follow_up)
    lab_tests = str(lab_tests)
    
    blood_pressure = int(blood_pressure)
    blood_glucose = int(blood_glucose)
    pulse = int(pulse)
    oxygen_level = int(oxygen_level)

    # Public Key input
    # n = int(input("Public key (n): "))
    # e = int(input("Public key (e): "))
    n = int(os.getenv("N"))
    e = int(os.getenv("E"))

    verified = verify_dr.__main__(dr_email, dr_pass)
    if(not verified):
        return {'status':0,'res':"Healthcare professional not verified"}
    else:
        print("Healthcare professional successfully verified")


    try:
        previous_record_hash = hashRecordTracker.get_patient_hash(patientId)
    except:
        print("no initial record for this patient")
        return {'status': False, 'res':"no record for this patient" }
    # start to deploy VisitRecord.sol
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


    with open("compiled_visit_record.json", "w") as file:
        json.dump(compiled_sol_v, file)


    # bytecode visit record
    visit_record_bytecode = compiled_sol_v["contracts"]["VisitRecord.sol"]["VisitRecord"]["evm"]["bytecode"]["object"]
    # abi visit record
    visit_record_abi = compiled_sol_v["contracts"]["VisitRecord.sol"]["VisitRecord"]["abi"]

    # create the contract for visit record
    VisitRecord = w3.eth.contract(
        abi=visit_record_abi, bytecode=visit_record_bytecode)

    visit = visit_record(patientId, age, weight, height, reason, diagnosis, referrals,
                        follow_up, lab_tests, blood_pressure, blood_glucose, pulse, oxygen_level,lab_test_results)

    # Encrpytion Process for patient
    dr_pub = rsa.PublicKey(n, e)
    visit_bytes = visit.to_byte()
    visit_encrypted = rsa.encrypt(visit_bytes, dr_pub)
    print("encrypted visit data: " + str(visit_encrypted))
    # Build, Sign, Send the transaction
    nonce = w3.eth.getTransactionCount(my_address)
    visit_record_transaction = VisitRecord.constructor(visit_encrypted, previous_record_hash['hash']).buildTransaction({
        "gasPrice": w3.eth.gas_price, "chainId": chain_id, "from": my_address, "nonce": nonce
    })
    signed_visit_record_trnxn = w3.eth.account.sign_transaction(
        visit_record_transaction, private_key=private_key)
    hashed_visit_record_trnxn = w3.eth.send_raw_transaction(
        signed_visit_record_trnxn.rawTransaction)
    visit_record_trnxn_receipt = w3.eth.wait_for_transaction_receipt(
        hashed_visit_record_trnxn)
    print("VISIT.....")
    print(visit_record_trnxn_receipt)
    print("hash.....")
    print(visit_record_trnxn_receipt['transactionHash'].hex())
    hash = visit_record_trnxn_receipt['transactionHash'].hex()

    # # Work with the visit record contract
    # # we need Contract Address, Contract ABI
    # visit_record = w3.eth.contract(
    #     address=visit_record_trnxn_receipt.contractAddress, abi=visit_record_abi)
    # print(visit_record.functions.readRecord().call())

    hashRecordTracker.set_patient_hash(patientId, hash)
    return {'status': True,'res':"visit recorded, trxn receipt  = " +str(visit_record_trnxn_receipt)}
