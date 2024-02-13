from pydantic import BaseModel

class Response(BaseModel):
    number: str
    name: str
    cnic: str
    address: str