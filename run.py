#!/usr/bin/env python3
"""
Run script for Expense Tracker
"""
import uvicorn
import os

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8999"))
    uvicorn.run("app.main:app", host="127.0.0.1", port=port, reload=True)
