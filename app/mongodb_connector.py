import os
from pymongo import MongoClient


class MongoDBConnector:
    def __init__(self) -> None:
        self.host =os.getenv("HOST", "localhost")
        self.port = int(os.getenv("PORT", "27017"))
        self.db_name = os.getenv("DB","contactsdb")       # Delete here - "",mongodb" used elsewhere
        self.collection_name = os.getenv("COLLECTION", "contacts")   # Delete here - ", contacts" used elsewhere
        uri = f'mongodb://{self.host}:{int(self.port)}/'
    
        self.client = MongoClient(uri)
        self.db = self.client[self.db_name]
        self.collection = self.db[self.collection_name]
        