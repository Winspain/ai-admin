import os
from pathlib import Path

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from src.auth import router
from src.database import register_tortoise

# 加载.env文件
load_dotenv()

app = FastAPI()

# 数据库初始化
register_tortoise(app)

# 添加路由
app.include_router(router.router)

if __name__ == '__main__':
    web_port = int(os.getenv('WEB_PORT'))
    current_path = Path(__file__).parent.parent
    log_path = f'{current_path}/logging.json'
    uvicorn.run('main:app', host='0.0.0.0', port=web_port, log_config=log_path)
