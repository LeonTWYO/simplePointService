from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from app.sql_config import app
from app.user_routes import user_blueprint
app.register_blueprint(user_blueprint, url_prefix='/user')

# if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8080)