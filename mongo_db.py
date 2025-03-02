from flask import Flask
import pymongo
from app import app

# Connection string from MongoDb Atlas
# CONN_STRING = "mongodb+srv://od_capstone:capPROJ123@cluster0.nrcft.mongodb.net/capstone-project?retryWrites=true&w=majority"
CONN_STRING = "mongodb+srv://shanu05official:8TrDA7j2Qs4isb3N@cluster0.otbkjtz.mongodb.net/?retryWrites=true&w=majority"
# CONN_STRING = "mongodb+srv://sheshnarayan:DrYFAe5nd5QAsjg0@cluster0.eux9sja.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"

# Initiating mongodb client
def open_mongo_diseases(index):
    client = pymongo.MongoClient(CONN_STRING)
    # Loading database
    db = client.get_database('cropguard')
    collection = db['cropguard-collection']

    # Disease data dictionary is sourced from the collection
    disease_data = collection.find_one({'Id': int(index)})

    # CLI: Printing the dictionary
    print(type(disease_data))

    # Closing the MongoDB session after sourcing data.
    client.close()
    return disease_data

def new_data(entry_name, caused_by, about, link, cure):
    # Adding the data in MongoDB
    # Opening connection
    client = pymongo.MongoClient(CONN_STRING)
    # Loading database
    db = client.get_database('cropguard')
    collection = db['cropguard-collection']

    # alert variable
    alert=''

    # Creating dictionary
    entry_dict = {
        "Name": entry_name,
        "Caused_by": caused_by,
        "About": about,
        "More_info_link": link,
        "Cure": cure
    }

    # Checking for duplicacy
    dupl_data = collection.find()

    # Variable to check if duplicate is present
    counter=0

    # Checking for redundancy
    for entry in dupl_data:
        if entry['Name'] == entry_name:
            print("Crop already entered by user.")
            alert = "Crop already entered by user."
            counter = 1
            break
    
    if counter == 0:
        # Inserting the dictionary
        collection.insert_one(entry_dict)

        print("Entry Successful")
        alert = "successful"

    # Closing the MongoDB session after inserting data.
    client.close()
    return alert