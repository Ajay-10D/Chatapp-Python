from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel


import requests


PRIVATE_KEY = "7fe27b47-92ed-42c3-a7e6-d4fc8fb9954c"
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    username: str

@app.post('/authenticate')
async def authenticate(user: User):
    response = requests.put('https://api.chatengine.io/users/',
        data={
            "username": user.username,
            "secret": user.username,
            "first_name": user.username,
        },
        headers={ "Private-key": PRIVATE_KEY }
    )
    return response.json()



# 7fe27b47-92ed-42c3-a7e6-d4fc8fb9954c