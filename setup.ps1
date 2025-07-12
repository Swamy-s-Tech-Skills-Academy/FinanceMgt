Write-Host "🚀 Setting up Finance Management App..." -ForegroundColor Green
Write-Host ""

Write-Host "📦 Activating virtual environment..." -ForegroundColor Yellow
& .\.venv\Scripts\Activate.ps1

Write-Host "📦 Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

Write-Host ""
Write-Host "✅ Setup complete!" -ForegroundColor Green
Write-Host "💡 To run the app: python run.py" -ForegroundColor Cyan
Write-Host "🛑 To deactivate venv: deactivate" -ForegroundColor Cyan
Write-Host ""
