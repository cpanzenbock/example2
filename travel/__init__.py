from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
db_filename = "travelDB.sqlite"


def create_app():
    app = Flask(__name__)
    app.secret_key = "Super Secret Key"
    bootstrap = Bootstrap(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_filename

    db.init_app(app)

    # add Blueprints
    from . import views

    app.register_blueprint(views.mainbp)

    from . import destinations

    app.register_blueprint(destinations.bp)

    return app
