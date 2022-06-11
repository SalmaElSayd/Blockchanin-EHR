from csv import writer
import dotenv
import rsa
from dotenv import load_dotenv
import os
import pandas
import ast
import csv

load_dotenv()
from Crypto.Cipher import AES
key = b'\x8f\xa2h\xe5\xa2\xcb&\x0c\xf2T\xe3\x954\xb9\xce\xf9'




# file_in = open("encrypted.bin", "rb")
# len(file_in)
# name, email, nonce, tag, ciphertext = [ file_in.read(x) for x in (1,1,16, 16, -1) ]
# print(name.decode('UTF-8'))
# print(email.decode('UTF-8'))
# # print(nonce)
# # print(tag)
# print(ciphertext)

#     # let's assume that the key is somehow available again
# cipher = AES.new(key, AES.MODE_EAX, nonce)
# data = cipher.decrypt_and_verify(ciphertext, tag)

# print(data)

import csv
content=[]
with open('testfile.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        content.append(line)

print(content)
ciphertext =  ast.literal_eval(content[0][-1])
nonce = ast.literal_eval(content[0][-3])
tag =  ast.literal_eval(content[0][-2])
print(tag)
cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)
print(data)
