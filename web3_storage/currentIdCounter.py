def get_current_id():
    f = open('idCounter.txt','r')
    id = int(f.readline())
    f.close()
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
