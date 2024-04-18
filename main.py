from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    score = {
        "Score": {
            "english": 24,
            "reading": 24,
            "science": 24,
            "math": 24
        }
    }

    return score