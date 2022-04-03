## Importing Essential Packages
from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_swagger_ui import get_swaggerui_blueprint
from api.config import ProductionConfig, DevelopmentConfig


# Basic Configurations for the Application
app = Flask(__name__)

if app.config["ENV"] == "production":
  app.config.from_object(ProductionConfig())
else:
  app.config.from_object(DevelopmentConfig())


# Datebase Configuration Initiation
db = SQLAlchemy(app)
ma = Marshmallow(app)


# Setting up routing Configurations
from api.sample.views import sample_blueprint
app.register_blueprint(sample_blueprint)


# Swagger UI Configuration Initiation
swaggerui_blueprint = get_swaggerui_blueprint(
  app.config['SWAGGER_URL'],
  app.config['SWAGGER_API_URL'],
  config={ 'app_name': "Swagger for the CRUD Application" }
)
app.register_blueprint(swaggerui_blueprint)


# Syncing all the DB Tables and creating system user
db.create_all()


# Error Handling Configuration Initiation
@app.errorhandler(404)
def page_not_found(e):
  return redirect('/api/docs')