from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class TopicCreate(BaseModel):
    title: str
    day: int
    status: Literal["not started", "in progress", "done"] = "not started"
    notes: str | None = None


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/topics")
def create_topic(topic: TopicCreate):
    return {"received": topic}