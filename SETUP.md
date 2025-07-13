# 🚀 Finance Management App - Setup Instructions

## 📋 Quick Setup

### Option 1: Using Setup Script (Recommended)

```bash
# For Command Prompt
setup.bat

# For PowerShell
.\setup.ps1
```

### Option 2: Manual Setup

```bash
# 1. Activate virtual environment
.\.venv\Scripts\activate    # Windows CMD
.\.venv\Scripts\Activate.ps1  # PowerShell

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
python run.py
```

## 📁 Updated Project Structure

```
d:\STSA\FinanceMgt/
├── .venv/                    # Virtual environment
├── src/
│   ├── instance/             # Database folder (moved here)
│   │   └── finance.db        # SQLite database (auto-created)
│   ├── app.py                # Main Flask application
│   ├── models.py             # Database models
│   ├── forms.py              # WTForms for user input
│   ├── config.py             # App configuration (updated path)
│   ├── templates/            # HTML templates
│   └── static/               # CSS and static files
├── requirements.txt          # Python dependencies
├── setup.bat                 # Windows setup script
├── setup.ps1                 # PowerShell setup script
├── run.py                    # Application runner
└── README.md                 # This file
```

## 🎯 What Changed

1. **Instance folder moved** from root to `src/instance/`
2. **Database path updated** in `config.py` to use relative path
3. **Virtual environment created** as `.venv/`
4. **Setup scripts added** for easy installation
5. **Run script updated** to handle the new structure

## 🌐 Running the App

1. **First time setup**: Run `setup.bat` or `setup.ps1`
2. **Subsequent runs**:
   ```bash
   .\.venv\Scripts\activate
   python run.py
   ```
3. **Open browser**: `http://127.0.0.1:5000`

## 🔧 Development Notes

- Virtual environment keeps dependencies isolated
- Database is now inside the `src` folder for better organization
- Setup scripts make it easy for others to run your project
- All paths are relative and should work across different systems

## 🚀 Ready to Code!

Your Finance Management App is now properly organized with a virtual environment. Perfect for your 45-minute coding session! 🎉
