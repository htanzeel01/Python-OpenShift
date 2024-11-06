from fastapi import APIRouter, HTTPException, status
from app.model.drinkrecord import DrinkRecord
from app.service.drinkrecordservice import get_drink_record
from typing import List

router = APIRouter(prefix="/api/drinkrecords", tags=["Drink Records"])

@router.get("/{patient_id}", response_model=List[DrinkRecord])
async def read_drink_record(patient_id: str):
    try:
        record = get_drink_record(patient_id=patient_id)  # Pass the necessary parameters
        if not record:
            raise HTTPException(status_code=404, detail="Drink record not found")
        return record
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
