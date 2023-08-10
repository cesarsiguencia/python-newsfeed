# from __init__ import create_app
import pymysql

pymysql.install_as_MySQLdb()

from routes import home, dashboard, api

from flask import Flask, jsonify

from db import init_db

from utils import filters

app = Flask(__name__, static_url_path='/')


    
app.url_map.strict_slashes = False
app.config.from_mapping(
    SECRET_KEY='super_secret_key'
)

app.jinja_env.filters['format_url'] = filters.format_url    
app.jinja_env.filters['format_date'] = filters.format_date
app.jinja_env.filters['format_plural'] = filters.format_plural

# register routes for blueprint 

app.register_blueprint(home)
app.register_blueprint(dashboard)
app.register_blueprint(api)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4999, debug=True)

init_db(app)
