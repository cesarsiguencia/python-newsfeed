from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g

load_dotenv()

# connect to database using env variable
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# loads seeds
def init_db(app):
    Base.metadata.create_all(engine) #build tables
    #close connection
    app.teardown_appcontext(close_db)

# gets info from database
def get_db():
    #so that we use the same session instead of returning Session everytime we declate this function, which would create a new Session on top of an already existing one
    if 'db' not in g:
        # store db connection in app context
        g.db = Session()
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()