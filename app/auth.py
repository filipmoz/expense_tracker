"""
Simple authentication for expense tracker
"""
from fastapi import HTTPException, Request, status
import secrets
import os

# Simple session storage (in production, use Redis or database)
active_sessions = set()

# User credentials (in production, use environment variables and hashed passwords)
USERNAME = os.getenv("EXPENSE_USERNAME", "user")
PASSWORD = os.getenv("EXPENSE_PASSWORD", "password123")  # Change this!

def verify_password(username: str, password: str) -> bool:
    """Verify user credentials"""
    return username == USERNAME and password == PASSWORD

def create_session() -> str:
    """Create a new session token"""
    session_token = secrets.token_urlsafe(32)
    active_sessions.add(session_token)
    return session_token

def verify_session(session_token: str) -> bool:
    """Verify if session token is valid"""
    return session_token in active_sessions

def remove_session(session_token: str):
    """Remove a session token"""
    active_sessions.discard(session_token)

async def get_current_user(request: Request):
    """Dependency to check if user is authenticated"""
    session_token = request.session.get("expense_session")
    
    if not session_token or not verify_session(session_token):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated. Please log in.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return {"username": USERNAME, "session": session_token}
