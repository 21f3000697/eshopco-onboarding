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

# Load data from file
with open("q-vercel-python.json") as f:
    marks_data = json.load(f)

@app.get("/api")
def get_marks(name: str = "", name2: str = ""):
    result = []
    if name in marks_data:
        result.append(marks_data[name])
    if name2 in marks_data:
        result.append(marks_data[name2])
    return {"marks": result}
