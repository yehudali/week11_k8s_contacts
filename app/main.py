from fastapi import FastAPI, HTTPException

from interactor import ContactBase

from interactor import MongoDBInteractor

db = MongoDBInteractor()
app = FastAPI()


    

@app.get("/")
def hello():
    return{"message" : "Welcome to Fastapi server!" }

@app.get("/contacts")
def get_contacts():
    try:
        return db.get_all_contacts()
    except Exception as e:
        return f"eror {e}"
    

@app.post("/contact")
def create_new_contact(contact_in : ContactBase):
    try:
        id = db.create_contact(contact_in)
        return id
    except Exception as err:
        return f'eror: {err}'


@app.put("/contacts/{id}")
def update(id,update:dict):
    try:
        return db.update_contact(id,update)
    except Exception as err:
        return f"Unexpected {err=}, {type(err)=}"


@app.delete("/contacts/{id}")
def delete(id):
    try:
        return db.delete_contact(id)
    except Exception as err:
        return f"Unexpected {err=}, {type(err)=}"


