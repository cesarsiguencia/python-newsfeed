from __init__ import create_app
import pymysql

pymysql.install_as_MySQLdb()

def start_app():
    create_app()



start_app()
