from flask import Flask

from datetime import datetime
from .models import read_build_script, connect,  create_database, fill_database
from flask_login import LoginManager

# connection a la db
conn = connect(database = "Reservation.sqlite")

# on cree la base -> Tables model SQL
create_database(conn)

# on rempli la base 
fill_database(conn)


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    
    #login_manager = LoginManager()
    #login_manager.login_view = 'auth.login'
    #login_manager.init_app(app)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app