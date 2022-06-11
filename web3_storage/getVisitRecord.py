from solcx import compile_standard
from web3 import Web3
import hashRecordTracker
import json
import solcx
import os
import csv
import rsa
from dotenv import load_dotenv
import verify_dr
load_dotenv()
solcx.install_solc('0.8.0')





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
def __main__(dr_email, dr_pass,patient_id):
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
    with open("./InitialRecord.sol", "r") as file:
        initial_record_file = file.read()

    compiled_sol_v_initial = compile_standard(
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
    
    visit_record_bytecode = compiled_sol_v["contracts"]["VisitRecord.sol"]["VisitRecord"]["evm"]["bytecode"]["object"]
    # abi visit record
    visit_record_abi = compiled_sol_v["contracts"]["VisitRecord.sol"]["VisitRecord"]["abi"]

    # bytecode visit record
    initial_record_bytecode = compiled_sol_v_initial["contracts"]["InitialRecord.sol"]["InitialRecord"]["evm"]["bytecode"]["object"]
    # abi visit record
    initial_record_abi = compiled_sol_v_initial["contracts"]["InitialRecord.sol"]["InitialRecord"]["abi"]

    verified = verify_dr.__main__(dr_email, dr_pass)
    if(not verified):
        print("Healthcare professional not verified")
        quit()
    else:
        print("Healthcare professional successfully verified")


    w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
    chain_id = 1337
    my_address =os.getenv("ADDRESS")
    private_key = os.getenv("PRIVATE_KEY")

    reached_end =False
    records = []


    # Getting the visit info
    try:
        curr_record_hash = hashRecordTracker.get_patient_hash(str(patient_id))['hash']
    except:
        print("Patient Id does not exist")
    else:
        # while(curr_record_hash != ''):
        while(not reached_end):

            print("------------------------------------")
            # Getting the transaction by the latest block
            transaction_receipt = w3.eth.get_transaction_receipt(
                curr_record_hash)

            VisitRecordContract = w3.eth.contract(
                abi=visit_record_abi, address=transaction_receipt.contractAddress)
            InitialRecordContract = w3.eth.contract(
                abi=initial_record_abi, address=transaction_receipt.contractAddress)

            try:
                # Reading the latest visit record
                enc_rec = VisitRecordContract.functions.readRecord().call()
            except:
                enc_rec = InitialRecordContract.functions.readRecord().call()
                reached_end = True
                # break
            print("encrypted record = "+str(enc_rec))
            # Decrypting the record using the private key
            dr_private_key = rsa.PrivateKey(int(os.getenv("N")), int(os.getenv(
                "E")), int(os.getenv("D")), int(os.getenv("P")), int(os.getenv("Q")))
            rec = rsa.decrypt(enc_rec[0], dr_private_key)

            # Decoding the bytes into string and print the record in a readable way
            rec_string = rec.decode("utf-8")
            rec_details = rec_string.split(',')
            if (not reached_end):
                print(print_visit_record(rec_details))
                data = {"id": rec_details[0],
                "age": rec_details[1],
                "weight": rec_details[2], 
                "height": rec_details[3],
                'Reason of visit: ': rec_details[4],
                'Diagnosis: ' : rec_details[5],
                'Referrals: ' : rec_details[6],
                'Follow-up: ' : rec_details[7],
                'Lab tests: ' : rec_details[8],
                'Blood Pressure: ' : str(rec_details[9]),
                'Blood Glucose: ' : str(rec_details[10]),
                'Pulse: ' : str(rec_details[11]),
                'Oxygen Level: ' : str(rec_details[12]) 
                }
                json_data = json.dumps(data)
                records.append(json_data)
                # updating the hash to get the previous visit
                curr_record_hash = enc_rec[1]
            else:
                print(print_init_record(rec_details))
                gender = 'Female'
                if(rec_details[5]):
                    gender = 'Male'
                data = {'Id': str(rec_details[0]) ,
            'Name' : rec_details[1] ,
            'Age' : str(rec_details[2]) ,
            'Weight' : str(rec_details[3]) ,
            'Height' : str(rec_details[4]) ,
            'Gender' : gender ,
            'Blood Pressure' : str(rec_details[6]) ,
            'Blood Glucose' : str(rec_details[7]) ,
            'Pulse' : str(rec_details[8]) ,
            'Oxygen Level' : str(rec_details[9])
                }
                json_data = json.dumps(data)
                records.append(json_data)
                break



            


    if len(records)>0:
        return {'status':True,'res':records}
    else:        # updating the hash to get the previous visit
        return {'status':False,'res':"No records for this patient"}

