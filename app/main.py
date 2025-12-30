from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# from .moduls import contact
from interactor import Datainteractor

db = Datainteractor()
app = FastAPI()

class ContactBase(BaseModel):
    first_name : str
    last_name : str
    phone_number : str


    

@app.get("/")
def hello():
    clietn = db.clietn()
    return{"message" : "Welcome to Fastapi server!" }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)


