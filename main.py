from fastapi import FastAPI, Depends
from database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.middleware.cors import CORSMiddleware
from model import YourTable
from sqlalchemy import delete, insert, select, update

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
async def main_route(number: int, db:AsyncSession = Depends(get_session)):
    entry = None
    async with db.begin():
        result = await db.execute(db.query(YourTable).filter(YourTable.number == number))
        entry = result.scalar_one_or_none()

    if entry is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"data": entry.dict()}
