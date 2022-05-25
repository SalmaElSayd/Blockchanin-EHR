def get_patient_hash(patientId): 
    import pandas
    hashdf = pandas.read_csv("patientHashes.csv",index_col="patientId")
    return hashdf.loc[patientId]

def set_patient_hash(patientId, new_hash): 
    import pandas
    hashdf = pandas.read_csv("patientHashes.csv",index_col="patientId")
    hashdf.loc[patientId] = new_hash
    hashdf.to_csv("patientHashes.csv")




