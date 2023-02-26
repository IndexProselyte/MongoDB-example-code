from pymongo import MongoClient
import time
from datetime import datetime
import random


def get_database():
   client = MongoClient(CONNECTION_STRING)
   print("Connected to the Atlas.\n")
   return client['sample_airbnb']
      
name, passw = input("Name: "), input("Password: ")
CONNECTION_STRING = f"mongodb+srv://{name}:{passw}@tester.e4ggbkl.mongodb.net/?retryWrites=true&w=majority"
# Get the database
dbname = get_database()
martin_data = dbname["martin_data"]

  
while True:
    # Get data
    today = datetime.today()
    message = {}
    message["Time"] = today.strftime("%d/%m/%Y %H:%M:%S")
    message["Temp"] = str(random.randrange(-28, 130))
    message["Humidity"] = str(random.randrange(0, 100))
    message["Co2"] = str(random.randrange(0, 100))

    martin_data.insert_one(message)
    print(f"Inserted these values into the database:\n {message} ")
    time.sleep(5)

