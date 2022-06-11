from csv import writer
import dotenv
import rsa
from dotenv import load_dotenv
import os
import pandas
import ast

load_dotenv()
from Crypto.Cipher import AES
key = b'\x8f\xa2h\xe5\xa2\xcb&\x0c\xf2T\xe3\x954\xb9\xce\xf9'

def __main__(email, password):
    drdf = pandas.read_csv("doctors.csv",index_col="Email", encoding=None)
    try:
        correct_pass = drdf.loc[email]['Password']
    except:
        return False
    # dr_private_key = rsa.PrivateKey(int(os.getenv("N")), int(os.getenv(
            # "E")), int(os.getenv("D")), int(os.getenv("P")), int(os.getenv("Q")))
    print((correct_pass))
    dec_pass=correct_pass
    # dec_pass = rsa.decrypt(bytes(correct_pass,'UTF-8'), dr_private_key)
    # print(dec_pass)
    if (password==dec_pass):
        return True
    return False

    file_in = open("encrypted.txt", "rb")
    number=list(file_in.read(3))
    # name, email, nonce, tag, ciphertext = [ file_in.read(x) for x in (1,1,16, 16, -1) ]
    # print(name.decode('UTF-8'),)
    # print(email)
    # print(nonce)
    # print(tag)
    # print(ciphertext)
    print(number)

    # let's assume that the key is somehow available again
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    return data

