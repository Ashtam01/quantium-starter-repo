#!/bin/bash

# 1. Activate the virtual environment
source venv/bin/activate

# 2. Run the test suite
python -m pytest test_app.py

# 3. Check the exit code of the previous command ($?)
if [ $? -eq 0 ]; then
  echo "Tests passed!"
  exit 0
else
  echo "Tests failed!"
  exit 1
fi