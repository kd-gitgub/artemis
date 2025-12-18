import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

# ASGI application expected by Databricks Apps (Python type)
app = FastAPI()

# Serve static assets (logo.png, etc.) from the current folder
app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/")
def root():
    # Return the existing index.html
    with open("index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    uvicorn.run(app, host="0.0.0.0", port=port)
