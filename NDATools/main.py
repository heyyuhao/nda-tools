import threading
from fastapi import FastAPI

# import your Download class
from NDATools.Download import Download

app = FastAPI()

@app.get("/download")
def start_download():
    download = Download()
    download.start()
    return {"message": "Download started"}

# cd ConceptBottleneck/submodule/nda-tools
# ▶ uvicorn NDATools.main:app --host 0.0.0.0 --port 8001 --reload