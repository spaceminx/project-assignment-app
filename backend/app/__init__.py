from flask import Flask
from .database import db
from . import config

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    with app.app_context():
        from . import models
        from .routes import api
        from .startup import initialize_database

        initialize_database()
        app.register_blueprint(api)

    return app