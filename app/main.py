"""
Main FastAPI application for Expense Tracker
"""
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
import secrets
import os

from app.database import init_db
from app.routers import expenses
from app.auth import get_current_user, verify_password, create_session, remove_session

app = FastAPI(
    title="Expense Tracker",
    description="Personal finance tracker with statistics and Excel export",
    version="1.0.0"
)

# Add session middleware for authentication
app.add_middleware(SessionMiddleware, secret_key=secrets.token_urlsafe(32))

# Initialize database
init_db()

# Include routers
app.include_router(expenses.router, prefix="/api/expenses", tags=["Expenses"])

# Templates
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """Main expense tracker interface (requires authentication)"""
    try:
        await get_current_user(request)
        return templates.TemplateResponse("expenses.html", {"request": request})
    except HTTPException:
        return RedirectResponse(url="/login", status_code=302)

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    """Login page"""
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(request: Request):
    """Login endpoint"""
    form_data = await request.form()
    username = form_data.get("username", "")
    password = form_data.get("password", "")
    
    if verify_password(username, password):
        session_token = create_session()
        request.session["expense_session"] = session_token
        return RedirectResponse(url="/", status_code=302)
    else:
        return HTMLResponse(
            content="""
            <html>
                <body>
                    <h2>Login Failed</h2>
                    <p>Invalid username or password.</p>
                    <a href="/login">Try again</a>
                </body>
            </html>
            """,
            status_code=401
        )

@app.get("/logout")
async def logout(request: Request):
    """Logout endpoint"""
    session_token = request.session.get("expense_session")
    if session_token:
        remove_session(session_token)
        request.session.clear()
    
    return RedirectResponse(url="/login", status_code=302)

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8999"))
    uvicorn.run(app, host="127.0.0.1", port=port)
