from datetime import timedelta


class Config(object):
  DEBUG = False
  TESTING = False
  
  SECRET_KEY = 'OMylDbgL9a7x3Dt3Om0XdYvcv93ZNa7m'
  
  SITE_URL = ''
  SESSION_COOKIE_SECURE = True
  SQLALCHEMY_DATABASE_URI = 'sqlite:///static/db-prod.db'
  SQLALCHEMY_TRACK_MODIFICATIONS = False

  SWAGGER_URL = '/api/docs'
  SWAGGER_API_URL = '/static/swagger.yml'


class ProductionConfig(Config):
  pass

class DevelopmentConfig(Config):
  DEBUG = True
  SITE_URL = 'http://localhost:5000'
  
  SESSION_COOKIE_SECURE = False
  SQLALCHEMY_DATABASE_URI = 'sqlite:///static/db-dev.db'

class TestingConfig(Config):
  TESTING = True
  SITE_URL = 'http://localhost:5000'
  
  SESSION_COOKIE_SECURE = False