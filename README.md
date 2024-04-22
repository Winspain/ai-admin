```shell
cd /root
mkdir code
git clone https://github.com/Winspain/ai-admin.git
cd /src
pip install -r requirements.txt
```

<h3>带日志</h3>  

```shell
nohup /usr/local/bin/python3 -m uvicorn main:app --host 0.0.0.0 --port 60010 > /root/code/ai-admin/src/logfile.log 2>&1 &
```

<h3>不带日志</h3>  

```shell
nohup /usr/local/bin/python3 -m uvicorn main:app --host 0.0.0.0 --port 60010 > /dev/null 2>&1 &
```
