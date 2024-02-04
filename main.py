from fastapi import FastAPI
from database import engine
import model
model.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/") 
async def main_route():     
  return {"message": "Hey, It is me Goku"}