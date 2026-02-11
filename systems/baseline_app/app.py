from flask import Flask
from flask_login import LoginManager
from routes import register_routes

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret'

login_manager = LoginManager()
login_manager.init_app(app)

register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
