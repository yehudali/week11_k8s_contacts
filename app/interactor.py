import os
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
load_dotenv()


class Datainteractor:
    def __init__(self) -> None:
        self.db_name = os.getenv("DB","contactsdb")
        self.host =os.getenv("HOST", "localhost")
        self.port = int(os.getenv("PORT", "27017"))
        uri = f'mongodb://{self.host}:{int(self.port)}/'
    
        self.client = MongoClient(uri)
        self.db = self.client[self.db_name]
        self.collection =self.db["contacts"]



    

    



