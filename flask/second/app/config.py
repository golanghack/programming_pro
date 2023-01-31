#! usr/bin/env python3 

"""Configuration for second application."""

import os 
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Main class for configuration."""
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MYSITE_MAIL_SUBJECT_PREFIX = '[Mysite]'
    MYSITE_MAIL_SENDER = 'Mysite Admin mysite@admin.com'
    MYSITE_ADMIN = os.environ.get('MYSITE_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    @staticmethod
    def init_app(app):
        pass
    
class DeveloperConfig(Config):
    """Class for realisation main setting for developers."""
    
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
        
class TestingConfig(Config):
    """Class for configuration testing app."""
    
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite://'
    
class ProductionConfig(Config):
    """Configuration for production ready."""
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
        
config = {
    'development': DeveloperConfig,
    'testing': TestingConfig, 
    'production': ProductionConfig, 
    'default': DeveloperConfig,
}