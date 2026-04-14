from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Task(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, default='')
    priority    = db.Column(db.String(20), default='medium')
    due_date    = db.Column(db.Date, nullable=True)
    status      = db.Column(db.String(20), default='pending')
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at  = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
