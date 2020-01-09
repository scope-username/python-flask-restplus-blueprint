from flask import Flask
from flask_basicauth import BasicAuth
import os

from extensions import jwt
from blueprints.blueprint1.blueprint import blueprint as blueprint1
from blueprints.blueprint2.blueprint import blueprint as blueprint2

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = os.environ.get("BASIC_AUTH_USERNAME")
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get("BASIC_AUTH_PASSWORD")
app.config['BASIC_AUTH_FORCE'] = True
app.config['RESTPLUS_VALIDATE'] = True
app.config.SWAGGER_UI_REQUEST_DURATION = True

app.config['JWT_SECRET_KEY'] = os.environ.get("JWT_SECRET_KEY")
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = int(300)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = int(900)
app.config['JWT_ALGORITHM'] = 'HS512'
app.config['JWT_HEADER_NAME'] = 'Token'
app.config['JWT_HEADER_TYPE'] = ''

app.register_blueprint(blueprint1)
app.register_blueprint(blueprint2)

basic_auth = BasicAuth(app)
jwt.init_app(app)

app.run(debug=True, host='0.0.0.0')
