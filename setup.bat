@echo off
echo 🚀 Setting up Finance Management App...
echo.

echo 📦 Activating virtual environment...
call .venv\Scripts\activate.bat

echo 📦 Installing dependencies...
pip install -r requirements.txt

echo.
echo ✅ Setup complete! 
echo 💡 To run the app: python run.py
echo 🛑 To deactivate venv: deactivate
echo.
