from flask import Flask

from blueprints.blueprint1.blueprint import blueprint as blueprint1
from blueprints.blueprint2.blueprint import blueprint as blueprint2

app = Flask(__name__)

app.register_blueprint(blueprint1)
app.register_blueprint(blueprint2)

app.config.SWAGGER_UI_REQUEST_DURATION = True
app.run(debug=True)

# TODO adding authentication - https://flask-restplus.readthedocs.io/en/stable/swagger.html#documenting-authorizations
# TODO swagger documentation - https://flask-restplus.readthedocs.io/en/stable/swagger.html#input-and-output-models
