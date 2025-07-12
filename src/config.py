import os

class Config:
    SECRET_KEY = 'vibe-coding-finance-app'
    
    # Ensure instance directory exists
    instance_dir = os.path.join(os.path.dirname(__file__), 'instance')
    if not os.path.exists(instance_dir):
        os.makedirs(instance_dir)
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(instance_dir, 'finance.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
