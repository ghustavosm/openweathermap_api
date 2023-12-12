import os
import requests
from datetime import datetime
from app.utils.extensions import mongo
from requests.exceptions import RequestException
from app.utils.strings import API_REQUEST_FAILURE, MONGO_SAVE_ERROR, MONGO_READ_ERROR


def get_weather(city):
    try:
        params = {
            "q": city,
            "appid": os.getenv("OPENWEATHER_API_KEY"),
            "units": "metric",
        }
        response = requests.get(os.getenv("OPENWEATHER_API_BASE_URL"), params=params)
        response.raise_for_status()
        data = response.json()
    except RequestException as e:
        return {"error": API_REQUEST_FAILURE, "details": str(e)}

    try:
        mongo.db.api_call_history.insert_one(
            {"city": city, "datetime": datetime.now(), "data": data}
        )
    except Exception as e:
        return {"error": MONGO_SAVE_ERROR, "details": str(e)}

    return data


def get_history():
    try:
        records = mongo.db.api_call_history.find()
        return records
    except Exception as e:
        return {"error": MONGO_READ_ERROR, "details": str(e)}
