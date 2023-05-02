from app.routes import home, dashboard, api

from flask import Flask

from app.db import init_db

from app.utils import filters


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
    
    app.jinja_env.filters['format_url'] = filters.format_url    
    app.jinja_env.filters['format_date'] = filters.format_date
    app.jinja_env.filters['format_plural'] = filters.format_plural
    
    # register routes for blueprint 

    app.register_blueprint(home)
    app.register_blueprint(dashboard)
    app.register_blueprint(api)
    

    #let the flask app be create first before we connect to the database with the seeds

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=4999, debug=True)

    init_db(app)

    return app


# The app should serve any static resources from the root directory and not from the default /static directory.

# Trailing slashes are optional (meaning that /dashboard and /dashboard/ load the same route).

# The app should use the key called 'super_secret_key' when creating server-side sessions.