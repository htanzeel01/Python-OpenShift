from fastapi import APIRouter, HTTPException, status
from app.model.drinkrecord import DrinkRecord
from app.service.drinkrecordservice import add_drink_record, get_drink_record
from datetime import date

router = APIRouter(prefix="/api/drinkrecords", tags=["Drink Records"])

@router.post("/", response_model=DrinkRecord, status_code=status.HTTP_201_CREATED)
async def create_drink_record(record: DrinkRecord):
    try:
        record.date = date.today().isoformat()
        new_record = add_drink_record(record)
        return new_record
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


