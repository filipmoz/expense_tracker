# Expense Tracker

This personal finance tracker application is designed to help manage weekly budgets and expenses, specifically aimed at assisting students in monitoring their spending and adhering to budget constraints.

## About

As a student residing in Liverpool, I need to effectively manage a weekly budget set at £100. This application facilitates the tracking of all my expenditures, allows for analysis of spending patterns, and ensures I remain within my allocated budget each week.

## Features

- **Expense Tracking**: Easily add, view, modify, and delete expenses.
- **Statistics**: Access detailed statistics and trends regarding spending habits.
- **Excel Export**: Export expense data to Excel for additional analysis.
- **Budget Management**: Monitor expenditures in relation to weekly budget limits.
- **Charts & Visualizations**: Gain insights through visual representations of spending patterns.
- **Authentication**: Secure login system for user protection.

## Installation

For a quick setup, run `./setup.sh` then `./run.py` (use `chmod +x setup.sh run.py` if necessary).

Manual steps:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

The application runs on http://localhost:8999

## Usage

- Navigate to http://localhost:8999
- Log in using your credentials
- Record expenses throughout the week
- Track your spending against your £100 weekly budget
- Export data to Excel for comprehensive analysis

## Weekly Budget

Set your weekly budget at £100 and monitor expenses to ensure compliance with this limit. The application offers statistics and visualizations to enhance understanding of your spending habits.

## API Endpoints

- GET / - Main interface for expense tracking
- POST /api/expenses/ - Add a new expense
- GET /api/expenses/ - Retrieve all expenses
- GET /api/expenses/stats - Obtain spending statistics
- GET /api/expenses/export/excel - Export data to Excel

## Author

A student in Liverpool, managing a weekly budget of £100.
