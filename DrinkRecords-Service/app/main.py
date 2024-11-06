from fastapi import FastAPI
from app.controllers import messagecontroller

app = FastAPI()

# Register the controller routes
app.include_router(messagecontroller.router)
