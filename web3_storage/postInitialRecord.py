from solcx import compile_standard
from web3 import Web3
import json
import hashRecordTracker
import currentIdCounter
import solcx
import os
import rsa
from dotenv import load_dotenv
import verify_dr
load_dotenv()
solcx.install_solc('0.8.0')



def __main__(dr_email, dr_pass,name,age,weight,height,female,blood_pressure,blood_glucose,pulse,oxygen_level):
    import Initial_Record

# start to deploy InitialRecord.sol
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

    with open("compiled_initial_record.json", "w") as file:
        json.dump(compiled_sol, file)

    # bytecode initial record
    initial_record_bytecode = compiled_sol["contracts"]["InitialRecord.sol"]["InitialRecord"]["evm"]["bytecode"]["object"]
    # abi initial record
    initial_record_abi = compiled_sol["contracts"]["InitialRecord.sol"]["InitialRecord"]["abi"]

    # connect to blockchain ganache
    w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
    chain_id = 1337
    my_address =os.getenv("ADDRESS")
    private_key = os.getenv("PRIVATE_KEY")

    # create the contract for initial record
    InitialRecord = w3.eth.contract(
        abi=initial_record_abi, bytecode=initial_record_bytecode)


    verified = verify_dr.__main__(dr_email, dr_pass)
    if(not verified):
        return {'status':0,'res':"Healthcare professional not verified"}
    else:
        print("Healthcare professional successfully verified")


    # getting inputs
    patientId = currentIdCounter.get_current_id()
    # name = str(input("enter name: "))
    # age = int(input("enter age: "))
    # weight = int(input("enter weight: "))
    # height = int(input("height: "))
    # female = bool(input("female?: "))
    # blood_pressure = int(input("blood pressure: "))
    # blood_glucose = int(input("blood glucose: "))
    # pulse = int(input("pulse: "))
    # oxygen_level = int(input("oxygen level: "))

    name = str(name)
    age = int(age)
    weight = int(weight)
    height = int(height)
    female = int(female)
    blood_pressure = int(blood_pressure)
    blood_glucose = int(blood_glucose) 
    pulse = int(pulse)
    oxygen_level = int(oxygen_level) 


    # Public Key input
    # n = int(input("Public key (n): "))
    # e = int(input("Public key (e): "))
    n = int(os.getenv("N"))
    e = int(os.getenv("E"))
    patient = Initial_Record.initial_record(patientId, name, age, weight, height,
                            female, blood_pressure, blood_glucose, pulse, oxygen_level)

    # Encrpytion Process for patient
    dr_pub = rsa.PublicKey(n, e)
    patient_bytes = patient.to_byte()
    patient_encrypted = rsa.encrypt(patient_bytes, dr_pub)

    print(patient_encrypted)
    # Build, Sign, Send the transaction
    nonce = w3.eth.getTransactionCount(my_address)
    initial_record_transaction = InitialRecord.constructor(patient_encrypted).buildTransaction({
        "gasPrice": w3.eth.gas_price, "chainId": chain_id, "from": my_address, "nonce": nonce
    })
    signed_initial_record_trnxn = w3.eth.account.sign_transaction(
        initial_record_transaction, private_key=private_key)
    hashed_initial_record_trnxn = w3.eth.send_raw_transaction(
        signed_initial_record_trnxn.rawTransaction)
    initial_record_trnxn_receipt = w3.eth.wait_for_transaction_receipt(
        hashed_initial_record_trnxn)
    print("INITIAL.....")
    print(initial_record_trnxn_receipt)
    print(initial_record_abi)
    hash = initial_record_trnxn_receipt['transactionHash'].hex()

    # Work with the initial record contract
    # we need Contract Address, Contract ABI
    initial_record = w3.eth.contract(
        address=initial_record_trnxn_receipt.contractAddress, abi=initial_record_abi)
    # print(initial_record_abi)
    currentIdCounter.increment_current_id()
    hashRecordTracker.set_patient_hash(patientId, hash)
    return {'status':True,'res' :"new Initial record successfully added with Id"+ str(patientId)}
    # Reading the record with encryption (Reem)
    # print('Reading the initial record .....')
    # trnxn_receipt = initial_record_trnxn_receipt
    # InitialRecordContract = w3.eth.contract(
    #     abi=initial_record_abi, address=trnxn_receipt.contractAddress)

    # rec = InitialRecordContract.functions.readRecord().call()
    # print('Encrypted Record:')
    # print(rec)

    # dec_rec = rsa.decrypt(rec, dr_priv)
    # print('Decrypted Record:')
    # print(dec_rec)
