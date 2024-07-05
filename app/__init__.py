from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    
    from app import routes, models, auth, guide_routes
    app.register_blueprint(auth.bp)
    app.register_blueprint(guide_routes.bp)
    app.register_blueprint(routes.bp)

    return app


