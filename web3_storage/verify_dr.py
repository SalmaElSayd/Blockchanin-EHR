from csv import writer
import dotenv
import rsa
from dotenv import load_dotenv
import os
import pandas
import ast

load_dotenv()
from Crypto.Cipher import AES
key = ast.literal_eval(os.getenv('AES'))

def __main__(email, password):
    drdf = pandas.read_csv("doctors.csv",index_col="Email", encoding=None)
    try:
        record = drdf.loc[email]
        ciphertext =  ast.literal_eval(record['Password'])
        nonce = ast.literal_eval(record['Nonce'])
        tag =  ast.literal_eval(record['Tag'])
    except:
        return False
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    dec_pass = cipher.decrypt_and_verify(ciphertext, tag)
    if (bytes(password,'UTF-8')==dec_pass):
        return True
    return False
