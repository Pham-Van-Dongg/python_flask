from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# Khởi tạo các thành phần
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Load cấu hình từ config.py
    app.config.from_object('app.config.Config')

    # Khởi tạo database và JWT
    db.init_app(app)
    jwt.init_app(app)

    # Đăng ký các route
    from app.routes import main
    app.register_blueprint(main)

    return app
