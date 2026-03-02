#!/bin/bash

echo "Starting FastAPI server..."

uvicorn app:app --host 0.0.0.0 --port 8000 &

sleep 3

echo "Starting Streamlit UI..."

streamlit run UI/frontened.py --server.address=0.0.0.0 --server.port=8501