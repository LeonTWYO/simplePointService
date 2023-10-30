import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Use the DATABASE_URL environment variable if available; otherwise, use a default value
database_url = os.environ.get("DATABASE_URL", "postgresql://myuser:mypassword@localhost/mydb")
# Configure the database URI. Replace with your PostgreSQL database URI.
app.config['SQLALCHEMY_DATABASE_URI'] = database_url

# Initialize the SQLAlchemy extension
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

@app.route('/')
def hello():
    return jsonify(message="Hello, world!")
@app.route('/create_user', methods=['POST'])
def create_user():
    try:
        username = request.json['username']
        initial_balance = request.json['initial_balance']
        # Create a new user
        new_user = User(username=username, balance=initial_balance)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User created successfully"}), 201  # Use 201 status code for resource creation

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

    finally:
        db.session.close()
@app.route('/get_balance/<int:user_id>', methods=['GET'])
def get_balance(user_id):
    try:
        user = User.query.get(user_id)
        if user:
            return jsonify({"balance": user.balance}), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400
@app.route('/use_points', methods=['POST'])
def use_points():
    try:
        user_id = request.json['user_id']
        points = request.json['points']
        # Check if the user has enough points to use
        user = User.query.get(user_id)
        if user.balance >= points:
            # Update user's balance to use points
            user.balance -= points
            db.session.commit()

            # Insert a transaction record
            transaction = Transaction(user_id=user_id, transaction_type='use', points=points)
            db.session.add(transaction)
            db.session.commit()

            return jsonify({"message": "Points used successfully"}), 200
        else:
            return jsonify({"error": "Insufficient points to use"}), 400

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

    finally:
        db.session.close()
@app.route('/give_points', methods=['POST'])
def give_points():
    try:
        user_id = request.json['user_id']
        points = request.json['points']

        # Check if the user has enough points to give
        user = User.query.get(user_id)
        if user:
            # Update user's balance to give points
            user.balance += points
            db.session.commit()

            # Insert a transaction record
            transaction = Transaction(user_id=user_id, transaction_type='give', points=points)
            db.session.add(transaction)
            db.session.commit()

            return jsonify({"message": "Points given successfully"}), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
    
    finally:
        db.session.close()

# if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8080)