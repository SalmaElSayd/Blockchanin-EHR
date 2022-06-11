from csv import writer
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

# strdata = "abc"
# data = bytes(password,'UTF-8')
# key = b'\x8f\xa2h\xe5\xa2\xcb&\x0c\xf2T\xe3\x954\xb9\xce\xf9'
# print(key)
# cipher = AES.new(key, AES.MODE_EAX)
# ciphertext, tag = cipher.encrypt_and_digest(data)

# print(cipher.nonce, tag, ciphertext)

# file_out = open("encrypted.csv", "wb")
# [ file_out.write(x) for x in (bytes(name,'UTF-8'), bytes(email,'UTF-8'), cipher.nonce, tag, ciphertext) ]
# file_out.close()



enc_password = password

n = int(os.getenv('N'))
e = int(os.getenv('E'))

# dr_pub = rsa.PublicKey(n, e)
# password_bytes = bytes(password, "UTF-8")
# print(password_bytes)
# enc_password = rsa.encrypt(password_bytes, dr_pub)
# print(type(enc_password))
# import chardet
# the_encoding = chardet.detect(enc_password)
# print(str(bytes_data,'utf-8'))
print(enc_password)
dr_data  =[name,email,enc_password]
with open('doctors.csv', 'a', newline='') as f_object:  
    writer_object = writer(f_object)
    writer_object.writerow(dr_data)  
    f_object.close()