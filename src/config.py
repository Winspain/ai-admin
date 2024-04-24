from playhouse.pool import PooledMySQLDatabase
import os
from dotenv import load_dotenv

load_dotenv()

DB = PooledMySQLDatabase(
    os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    max_connections=8,  # 最大连接数
    stale_timeout=300,  # 连接在这个时间内未被使用则被关闭
)
