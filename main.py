from fastapi import FastAPI, Depends, HTTPException
from database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.middleware.cors import CORSMiddleware
from model import YourTable
from sqlalchemy import delete, insert, select, update, BigInteger, cast
app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/number/{number}") 
async def main_route(number: str, db:AsyncSession = Depends(get_session)):
    try:
        entry = None
        async with db.begin():
            result = await db.execute(select(YourTable).filter(YourTable.number == number))
            print('check result: ',result)
            entry = result.scalar_one_or_none()

        if entry is None:
            raise HTTPException(status_code=404, detail="Item not found")

        return {"data": {
            "id": entry.id,
            "number": entry.number,
            "name": entry.name,
            "cnic": entry.cnic,
            "address": entry.address
        }}
    except Exception as error:
        raise HTTPException(status_code=404, detail=str(error))


@app.get("/api/cnic/{cnic}") 
async def main_route(cnic: str, db:AsyncSession = Depends(get_session)):
    try:
        entry = None
        async with db.begin():
            result = await db.execute(select(YourTable).filter(YourTable.cnic == cnic))
            print('check result: ',result)
            entry = result.scalar_one_or_none()

        if entry is None:
            raise HTTPException(status_code=404, detail="Item not found")

        return {"data": {
            "id": entry.id,
            "number": entry.number,
            "name": entry.name,
            "cnic": entry.cnic,
            "address": entry.address
        }}
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))