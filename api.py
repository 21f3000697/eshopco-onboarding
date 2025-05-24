from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data from file (list of dicts)
with open("q-vercel-python.json") as f:
    marks_data = json.load(f)

@app.get("/api")
def get_marks(name: str = "", name2: str = ""):
    result = []
    for entry in marks_data:
        if entry["name"] == name:
            result.append(entry["marks"])
        if name2 and entry["name"] == name2 and name2 != name:
            result.append(entry["marks"])
    return {"marks": result}

# Optional: root endpoint for friendly message
@app.get("/")
def root():
    return {"message": "API is running! Use /api?name=...&name2=..."}

