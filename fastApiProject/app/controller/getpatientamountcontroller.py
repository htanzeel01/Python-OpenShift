from fastapi import APIRouter, HTTPException, status
from app.service.patientservice import get_daily_goal_by_id

router = APIRouter(prefix="/api/patients", tags=["Patients"])

@router.get("/{patient_id}/daily_goal", response_model=float)
async def read_daily_goal(patient_id: str):
    try:
        daily_goal = get_daily_goal_by_id(patient_id=patient_id)
        return daily_goal
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
