from flask import Blueprint, request
from app.controllers.weather_controller import get_weather_data, get_history_data
from app.utils.strings import WELCOME_MESSAGE

api_routes = Blueprint("api_routes", __name__)


@api_routes.route("/")
def index():
    return WELCOME_MESSAGE


@api_routes.route("/weather")
def weather():
    city = request.args.get("city", "Brasília")
    return get_weather_data(city)


@api_routes.route("/history")
def history():
    return get_history_data()
