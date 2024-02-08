from flask import Flask
from src.main.routes.tag_routes import tag_blueprint_routes

app = Flask(__name__)
app.register_blueprint(tag_blueprint_routes)
