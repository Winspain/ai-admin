#!/bin/bash

# 启动 Python 脚本并将输出保存到 output.log 中
nohup python3 src/main.py > output.log 2>&1 &

# 输出进程ID
echo "src/main.py has been started with PID: $!"
