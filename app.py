import os
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

# ASGI application expected by Databricks Apps (Python type)
app = FastAPI()

# Get the directory where app.py is located
app_dir = Path(__file__).parent

@app.get("/")
def root():
    # Return the existing index.html from the app directory
    html_file = app_dir / "index.html"
    with open(html_file, "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())

@app.get("/health")
def health():
    return {"status": "ok"}

# Serve all other files (logo.png, etc.) from the app directory
app.mount("/", StaticFiles(directory=str(app_dir)), name="static")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    uvicorn.run(app, host="0.0.0.0", port=port)
