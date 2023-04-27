from app.routes import home, dashboard

from flask import Flask

from app.db import init_db

def create_app(test_config=None):
    # set up createApp
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    app.config.from_mapping(
        SECRET_KEY='super_secret_key'
    )

    @app.route('/hello')
    def hello():
        return 'hello world'
    
    # register routes for blueprint 
    app.register_blueprint(home)
    app.register_blueprint(dashboard)

    init_db(app)

    return app


# The app should serve any static resources from the root directory and not from the default /static directory.

# Trailing slashes are optional (meaning that /dashboard and /dashboard/ load the same route).

# The app should use the key called 'super_secret_key' when creating server-side sessions.