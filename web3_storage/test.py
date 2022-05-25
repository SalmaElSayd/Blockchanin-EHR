import hashRecordTracker
import json
import solcx
import os
import csv
from dotenv import load_dotenv
load_dotenv()
from web3 import Web3
solcx.install_solc('0.8.0') 
from solcx import compile_standard
print(hashRecordTracker.set_patient_hash(3,"xcv"))

# w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
# chain_id = 1337
# my_address = "0x9d5A2f02E11793A196209e8055382b0895e1CE0A"
# private_key = os.getenv("PRIVATE_KEY")

# print(w3.eth.getTransaction('0xe4b33f7721785e7d404221cbcb494d06231c60f434d2943acbe0da5bab1fe22b'))
