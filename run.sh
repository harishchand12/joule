#!/bin/bash

echo "Setting up the database..."
sqlite3 school.db < database_schema.sql

echo "Installing backend dependencies..."
pip install -r school_management/backend/app/requirements.txt

echo "Installing frontend dependencies..."
cd school_management/frontend && npm install && cd ../..

echo "Setup complete. Please start the backend and frontend servers in separate terminals."
