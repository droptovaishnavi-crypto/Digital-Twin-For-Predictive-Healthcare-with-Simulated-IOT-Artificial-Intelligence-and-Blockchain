# run_fastapi.py
import uvicorn
import os
import sys

# Add the folder containing main.py to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
