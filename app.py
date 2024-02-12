from flask import Flask
import os
import psutil

app = Flask(__name__)

@app.route("/")
def home():
    return f"Project"

@app.route("/ping")
def ping():
    return f"200 OK"

@app.route("/healthz")
def cpu_util():
    pid  = os.getpid()
    process = psutil.Process(pid)

    mem_info=process.memory_info()

    rss = mem_info.rss
    vms = mem_info.vms
    cpu = process.cpu_percent(interval=1)
    return f"200 rss: {rss} bytes \n vms: {vms} bytes \n cpu usage: {cpu}%  "

if __name__== "__main__":
    app.run(debug=True)