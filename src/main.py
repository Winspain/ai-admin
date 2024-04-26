from fastapi import FastAPI, HTTPException

from src.database import register_tortoise
from src.auth import router

app = FastAPI()

# 数据库初始化
register_tortoise(app)

# 添加路由
app.include_router(router.router)
