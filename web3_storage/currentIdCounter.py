import rsa
import os
from dotenv import load_dotenv
import random

def get_current_id():
    f = open('idCounter.txt','r')
    id = f.readline()
    f.close()
    load_dotenv()
    id = str(id) +"-" + str(random.randint(100, 10000))
    return id

def increment_current_id():
    f = open('idCounter.txt','r')
    id = int(f.readline())
    f.close()
    f = open('idCounter.txt','w')
    new_id = str(int(id)+1)
    print(new_id)
    f.write(new_id)
    f.close()
