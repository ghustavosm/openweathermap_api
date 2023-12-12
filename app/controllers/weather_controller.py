from app.models.weather import get_weather, get_history
from bson import json_util
from flask import Response, jsonify


def get_weather_data(city="London"):
    result = get_weather(city)
    if "error" in result:
        return jsonify(result), 500
    return jsonify(result)


def get_history_data():
    records = get_history()
    if isinstance(records, dict) and "error" in records:
        return jsonify(records), 500
    return Response(json_util.dumps(records), content_type="application/json")
