from fastapi import FastAPI, HTTPException
from peewee import DoesNotExist

from models import ChatGPTUser
from scheme import TokenRequest

app = FastAPI()


@app.post("/aixian/v1/user")
async def get_user_expire_time(token_request: TokenRequest):
    try:
        user = ChatGPTUser.get(ChatGPTUser.userToken == token_request.userToken)
        return {"userToken": user.userToken, "expireTime": user.expireTime}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="User not found")