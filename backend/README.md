# InsightFlow AI Backend

## Overview
Backend API built with FastAPI.

## Requirements
- Python 3.12+

## Setup
Activate the virtual environment from the repository root:

source backend/.venv/Scripts/activate

Install dependencies:

python -m pip install -r backend/requirements.txt

## Run the server
From the backend directory:

python -m uvicorn app.main:app --reload

## API Endpoints
- GET /health — returns the API health status.

## Run tests
From the backend directory:

python -m pytest -v