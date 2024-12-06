"""
Main FastAPI application
"""
from fastapi import FastAPI
from app.database import init_db
from app.routers import expenses

app = FastAPI(title="Expense Tracker", version="0.1.0")
init_db()

app.include_router(expenses.router, prefix="/api/expenses")

@app.get("/")
async def root():
    return {"message": "Expense Tracker API"}
