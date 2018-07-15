from flask import (
    Flask,
    jsonify
)

from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate


app = Flask(__name__)


app.config.from_object('config')


db = SQLAlchemy(app)


migrate = Migrate(app, db)


@app.after_request
def after_request(response):
    response.headers.add(
        'Access-Control-Allow-Origin',
        '*'
    )

    response.headers.add(
        'Access-Control-Allow-Headers',
        'Content-Type, Authorization'
    )

    response.headers.add(
        'Access-Control-Allow-Methods',
        'GET, POST, PUT, DELETE, OPTIONS'
    )

    return response


@app.errorhandler(404)
def not_found(error):
    return jsonify(error=404), 404


from app.materials.views import materials


app.register_blueprint(materials, url_prefix='/materials')
