#!/bin/sh
python3 app.py > /dev/null 2>&1
git add .
git commit -m "Updated Links"
git push -u origin main
