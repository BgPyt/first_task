from fastapi import FastAPI
from src.quiz.router import app as router_quiz
import uvicorn

app = FastAPI()


app.include_router(router_quiz)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.0", port=8000)