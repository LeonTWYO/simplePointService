from flask import Blueprint, jsonify, request
from app.sql_config import db,User, Transaction

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/create_user', methods=['POST'])
def create_user():
    try:
        data = request.json
        username = data.get('username')
        initial_balance = data.get('initial_balance')

        if not username or not isinstance(username, str):
            return jsonify({"error": "Invalid or missing 'username' parameter"}), 400

        if initial_balance is None or not isinstance(initial_balance, int):
            return jsonify({"error": "Invalid or missing 'initial_balance' parameter"}), 400

        new_user = User(username=username, balance=initial_balance)
        db.session.add(new_user)
        db.session.commit()

        db.session.refresh(new_user)

        return jsonify({"message": "User created successfully", "user_id": new_user.user_id}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

    finally:
        db.session.close()

@user_blueprint.route('/use_points', methods=['POST'])
def use_points():
    try:
        data = request.json
        user_id = data.get('user_id')
        points = data.get('points')

        if user_id is None or not isinstance(user_id, int):
            return jsonify({"error": "Invalid or missing 'user_id' parameter"}), 400

        if points is None or not isinstance(points, int):
            return jsonify({"error": "Invalid or missing 'points' parameter"}), 400

        user = User.query.get(user_id)

        if user and user.balance >= points:
            user.balance -= points
            db.session.commit()

            transaction = Transaction(user_id=user_id, transaction_type='use', points=points)
            db.session.add(transaction)
            db.session.commit()

            return jsonify({"message": "Points used successfully"}), 200
        else:
            return jsonify({"error": "Insufficient points or user not found"}), 400

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

    finally:
        db.session.close()

@user_blueprint.route('/give_points', methods=['POST'])
def give_points():
    try:
        data = request.json
        user_id = data.get('user_id')
        points = data.get('points')

        if user_id is None or not isinstance(user_id, int):
            return jsonify({"error": "Invalid or missing 'user_id' parameter"}), 400

        if points is None or not isinstance(points, int):
            return jsonify({"error": "Invalid or missing 'points' parameter"}), 400

        user = User.query.get(user_id)

        if user:
            user.balance += points
            db.session.commit()

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

@user_blueprint.route('/get_balance/<int:user_id>', methods=['GET'])
def get_balance(user_id):
    try:
        if user_id is None:
            return jsonify({"error": "Missing 'user_id' parameter"}), 400

        user = User.query.get(user_id)
        if user:
            return jsonify({"balance": user.balance}), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@user_blueprint.route('/get_latest_transactions/<int:user_id>', methods=['GET'])
def get_latest_transactions(user_id):
    try:
        if user_id is None:
            return jsonify({"error": "Missing 'user_id' parameter"}), 400

        user = User.query.get(user_id)

        if not user:
            return jsonify({"error": "User not found"}), 404

        # Retrieve the latest 10 transaction records for the user
        latest_transactions = Transaction.query.filter_by(user_id=user_id).order_by(Transaction.transaction_time.desc()).limit(10).all()

        # Convert the transactions to a list of dictionaries
        transaction_list = []
        for transaction in latest_transactions:
            transaction_list.append({
                "transaction_id": transaction.transaction_id,
                "transaction_type": transaction.transaction_type,
                "points": transaction.points,
                "transaction_time": transaction.transaction_time
            })

        return jsonify({"transactions": transaction_list}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400