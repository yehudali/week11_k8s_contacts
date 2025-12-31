from dotenv import load_dotenv
from pydantic import BaseModel
from mongodb_connector import MongoDBConnector 
from bson import ObjectId
load_dotenv()


class ContactBase(BaseModel):
    first_name : str
    last_name : str
    phone_number : str

    def get_dict(self):
        return {"first_name":self.first_name,
                "last_name":self.last_name,"phone_number":self.phone_number}


class MongoDBInteractor:
    def __init__(self) -> None:
        self.db_connector =  MongoDBConnector()
         


    def create_contact(self, contact_data: ContactBase) -> str:
        document = contact_data.model_dump()
        result = self.db_connector.collection.insert_one(document)
        return str(result.inserted_id)

        
    def get_all_contacts(self) -> list[ContactBase]:
        cursor = self.db_connector.collection.find()
        result = []
        for doc in cursor:
            result.append({"id":str(doc["_id"]),"first name":doc["first_name"],"last name":doc["last_name"],"phone number":doc["phone_number"]})
            print(result)
        return result

    
    def update_contact(self, id ,update:dict):
        exists = self.db_connector.collection.count_documents({"_id": id}, limit=1) <= 0
        if exists:
            self.db_connector.collection.update_one({"_id": ObjectId(id)},{"$set": update})
            return True
        else:
            raise TypeError("ID number not found")

    def delete_contact(self, id):
        exists = self.db_connector.collection.count_documents({"_id": id}, limit=1) <= 0
        if exists:
            self.db_connector.collection.delete_one({"_id": ObjectId(id)})
            return True
        else:
            raise TypeError("ID number not found")
        






