from fastapi import FastAPI, HTTPException

from src.config import register_tortoise
from src.routers import user_router

app = FastAPI()

# 数据库初始化
register_tortoise(app)

# 添加路由
app.include_router(user_router.router)
