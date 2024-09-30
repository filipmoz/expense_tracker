"""
Pydantic schemas for Expense Tracker
"""
from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Optional

class ExpenseCreate(BaseModel):
    """Schema for creating an expense"""
    amount: float = Field(..., gt=0, description="Expense amount (must be positive)")
    category: str = Field(..., min_length=1, max_length=50, description="Expense category")
    description: Optional[str] = Field(None, max_length=500, description="Optional description")
    date: Optional[datetime] = Field(default_factory=datetime.utcnow, description="Expense date")

class ExpenseUpdate(BaseModel):
    """Schema for updating an expense"""
    amount: Optional[float] = Field(None, gt=0)
    category: Optional[str] = Field(None, min_length=1, max_length=50)
    description: Optional[str] = Field(None, max_length=500)
    date: Optional[datetime] = None

class ExpenseResponse(BaseModel):
    """Schema for expense response"""
    id: int
    amount: float
    category: str
    description: Optional[str]
    date: datetime
    created_at: datetime

    class Config:
        from_attributes = True

class ExpenseStats(BaseModel):
    """Schema for expense statistics"""
    total_expenses: float
    total_count: int
    average_expense: float
    median_expense: float
    min_expense: float
    max_expense: float
    std_deviation: float
    category_breakdown: dict[str, float]
    category_counts: dict[str, int]
