from uvicorn import run

from app import app

if __name__ == "__main__":
    run("app:app", host="0.0.0.0", port=8000, reload=True)
