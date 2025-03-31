"""
Statistics and analysis functions using numpy
"""
import numpy as np
from typing import List, Dict
from sqlalchemy.orm import Session
from app.models import Expense

def calculate_expense_statistics(db: Session) -> Dict:
    """Calculate comprehensive statistics for expenses"""
    expenses = db.query(Expense).all()
    
    if not expenses:
        return {
            "total_expenses": 0.0,
            "total_count": 0,
            "average_expense": 0.0,
            "median_expense": 0.0,
            "min_expense": 0.0,
            "max_expense": 0.0,
            "std_deviation": 0.0,
            "category_breakdown": {},
            "category_counts": {}
        }
    
    # Extract amounts as numpy array
    amounts = np.array([exp.amount for exp in expenses])
    
    # Basic statistics using numpy
    total_expenses = float(np.sum(amounts))
    total_count = len(expenses)
    average_expense = float(np.mean(amounts))
    median_expense = float(np.median(amounts))
    min_expense = float(np.min(amounts))
    max_expense = float(np.max(amounts))
    std_deviation = float(np.std(amounts))
    
    # Category breakdown
    category_breakdown = {}
    category_counts = {}
    
    for expense in expenses:
        category = expense.category
        if category not in category_breakdown:
            category_breakdown[category] = 0.0
            category_counts[category] = 0
        category_breakdown[category] += expense.amount
        category_counts[category] += 1
    
    return {
        "total_expenses": total_expenses,
        "total_count": total_count,
        "average_expense": average_expense,
        "median_expense": median_expense,
        "min_expense": min_expense,
        "max_expense": max_expense,
        "std_deviation": std_deviation,
        "category_breakdown": category_breakdown,
        "category_counts": category_counts
    }

def calculate_category_statistics(db: Session, category: str) -> Dict:
    """Calculate statistics for a specific category"""
    expenses = db.query(Expense).filter(Expense.category == category).all()
    
    if not expenses:
        return {
            "category": category,
            "total": 0.0,
            "count": 0,
            "average": 0.0,
            "median": 0.0,
            "min": 0.0,
            "max": 0.0
        }
    
    amounts = np.array([exp.amount for exp in expenses])
    
    return {
        "category": category,
        "total": float(np.sum(amounts)),
        "count": len(expenses),
        "average": float(np.mean(amounts)),
        "median": float(np.median(amounts)),
        "min": float(np.min(amounts)),
        "max": float(np.max(amounts))
    }
