from fastapi import APIRouter, HTTPException
from app.service.emailservice import send_email
from app.service.smsservice import send_sms

router = APIRouter()

@router.post("/send-message")
def send_message(message_type: str, recipient: str, subject: str = "", content: str = ""):
    try:
        if message_type == "email":
            send_email(recipient, subject, content)
        elif message_type == "sms":
            send_sms(recipient, content)
        else:
            raise HTTPException(status_code=400, detail="Invalid message type")
        return {"status": "Message sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
