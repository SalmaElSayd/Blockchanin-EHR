from csv import writer
import csv
import dotenv
import rsa
from dotenv import load_dotenv
import os
load_dotenv()
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes



name = str(input("Enter New Dr Name: "))
email = str(input("Enter New Dr Email: "))
password = str(input("Enter New Dr Password: "))


data = bytes(password,'UTF-8')
key = b'\x8f\xa2h\xe5\xa2\xcb&\x0c\xf2T\xe3\x954\xb9\xce\xf9'
print(key)
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

print(cipher.nonce, tag, ciphertext)

row =[name , email,str(cipher.nonce) , str(tag) , str(ciphertext)]
# open the file in the write mode
with open('testfile.csv', 'a') as f:
    # create the csv writer
    writer = csv.writer(f)
    # write a row to the csv file
    writer.writerow(row)
