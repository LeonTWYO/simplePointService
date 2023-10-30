from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

app = Flask(__name__)

# Use the DATABASE_URL environment variable if available; otherwise, use a default value
database_url = os.environ.get("DATABASE_URL", "postgresql://myuser:mypassword@localhost/mydb")
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
db = SQLAlchemy(app)
class User(db.Model):
    __tablename__ = 'users'  # Specify the table name explicitly
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    balance = db.Column(db.Integer, default=0)

class Transaction(db.Model):
    __tablename__ = 'transactions'  # Specify the table name explicitly
    transaction_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    transaction_type = db.Column(db.String(50), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    transaction_time = db.Column(db.TIMESTAMP, default=db.func.current_timestamp(), server_default=db.func.current_timestamp())
