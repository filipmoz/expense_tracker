"""
Main FastAPI application
"""
from fastapi import FastAPI
from app.database import init_db

app = FastAPI(title="Expense Tracker", version="0.1.0")
init_db()

@app.get("/")
async def root():
    return {"message": "Expense Tracker API"}
