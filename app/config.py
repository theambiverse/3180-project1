import os

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://p1:password@localhost/p1' or 'postgresql://jtcaqqfqsqtgpl:dfc3cd74b59f87bf565c4006d7b2a41ccf0ddbd3ec6210a8ca79c5683df27dd8@ec2-35-171-57-132.compute-1.amazonaws.com:5432/ddmov9gf46r3i9'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    UPLOAD_FOLDER='./uploads'
    
class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False