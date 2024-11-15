import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_photoPair():
    return {"id": 1,
            "image": "hyunjin.jpg",
            "keywords": ["hyunjin", "boyfriend"]
            }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)