# Expense Tracker

Personal finance tracker application for managing weekly budgets and expenses. Designed for students to track spending and stay within budget limits.

## About

As a student in Liverpool, I need to manage my weekly budget of £100. This application helps me track all my expenses, analyze spending patterns, and ensure I stay within my weekly budget limit.

## Features

- 📝 **Expense Tracking**: Add, view, edit, and delete expenses
- 📊 **Statistics**: View spending statistics and trends
- 📥 **Excel Export**: Export expenses to Excel for further analysis
- 💰 **Budget Management**: Track expenses against weekly budget limits
- 📈 **Charts & Visualizations**: Visual representation of spending patterns
- 🔐 **Authentication**: Secure login system

## Quick Start with Docker

### Prerequisites
- Docker and Docker Compose installed

### Start the Container

To start the application on port 8999:

```bash
docker compose up -d
```

The application will be available at: **http://localhost:8999**

### Stop the Container

```bash
docker compose down
```

### View Logs

```bash
docker compose logs -f
```

## Manual Setup

### 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python run.py
```

The application will start on port 8999 by default.

## Usage

1. Navigate to http://localhost:8999
2. Login with your credentials
3. Add expenses throughout the week
4. Monitor your spending against your £100 weekly budget
5. Export data to Excel for detailed analysis

## Weekly Budget

Set your weekly budget to £100 and track expenses to ensure you stay within your limit. The application provides statistics and visualizations to help you understand your spending patterns.

## API Endpoints

- `GET /` - Main expense tracking interface
- `POST /api/expenses/` - Add new expense
- `GET /api/expenses/` - Get all expenses
- `GET /api/expenses/stats` - Get spending statistics
- `GET /api/expenses/export/excel` - Export to Excel

## Author

Student in Liverpool, managing weekly budget of £100.
