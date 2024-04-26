```shell
mkdir /root/code && cd /root/code
git clone https://github.com/Winspain/ai-admin.git
vim /ai-admin/.env # add mysql password
pip install -r /ai-admin/src/base.txt
nohup /usr/local/bin/python3 -m uvicorn ai-admin.src.main:app --host 0.0.0.0 --port 60010 > /root/code/ai-admin/src/logfile.log 2>&1 &
```

<h3>带日志</h3>  

```shell
nohup /usr/local/bin/python3 -m uvicorn src.main:app --host 0.0.0.0 --port 60010 > /root/code/ai-admin/src/logfile.log 2>&1 &
```

<h3>不带日志</h3>  

```shell
nohup /usr/local/bin/python3 -m uvicorn src.main:app --host 0.0.0.0 --port 60010 > /dev/null 2>&1 &
```
