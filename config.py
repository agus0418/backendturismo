import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'turismo_secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://turismocodoacodo:turismodatabase@turismocodoacodo.mysql.pythonanywhere-services.com/turismocodoacodo$turismodb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
