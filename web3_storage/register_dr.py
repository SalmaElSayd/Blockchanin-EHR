from csv import writer
import dotenv
import rsa
from dotenv import load_dotenv
import os
load_dotenv()
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import ast


name = str(input("Enter New Dr Name: "))
email = str(input("Enter New Dr Email: "))
password = str(input("Enter New Dr Password: "))


data = bytes(password,'UTF-8')
key = ast.literal_eval(os.getenv('AES'))
print(key)
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

dr_data  =[name,email,str(cipher.nonce) , str(tag) , str(ciphertext)]
with open('doctors.csv', 'a', newline='') as f_object:  
    writer_object = writer(f_object)
    writer_object.writerow(dr_data)  
    f_object.close()


