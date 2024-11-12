from flask import Flask
from routes.home import home_route
from routes.register import register_route
from routes.login import login_route
from routes.data import data_route

app = Flask(__name__)
app.config.from_pyfile('config.py')

app.register_blueprint(home_route)
app.register_blueprint(register_route, url_prefix="/register")
app.register_blueprint(login_route, url_prefix="/login")
app.register_blueprint(data_route, url_prefix="/data")
app.run(debug=True)
