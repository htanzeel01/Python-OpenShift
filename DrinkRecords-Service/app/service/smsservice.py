from twilio.rest import Client

TWILIO_ACCOUNT_SID = "your_account_sid"
TWILIO_AUTH_TOKEN = "your_auth_token"
TWILIO_PHONE_NUMBER = "your_twilio_phone_number"

def send_sms(recipient: str, content: str):
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=content,
            from_=TWILIO_PHONE_NUMBER,
            to=recipient
        )
        return message.sid
    except Exception as e:
        raise Exception(f"Failed to send SMS: {e}")
