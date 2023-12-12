import os
from flask import Flask
from app.routes.api_routes import api_routes
from app.utils.extensions import mongo

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo.init_app(app)

app.register_blueprint(api_routes)
