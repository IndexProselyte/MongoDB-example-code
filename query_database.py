from pymongo import MongoClient

print("Connecting to the Atlas.")
uri = "mongodb+srv://dongo:bongo@tester.e4ggbkl.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri); 

# Choose the desired database
database = client.sample_airbnb
collection = database.martin_data

print("Searching the database...\n")
cursor = collection.find({"Time": "26/02/2023"}) 

# THE FIND FUNCTION RETURNS A DICTIONARY NOT A STRING!!!
for doc in cursor:
    if int(doc["Co2"]) > 25:
        print("Dangerously high Co2 levels in this entry: ")
        print(doc)
        print("")

client.close()
