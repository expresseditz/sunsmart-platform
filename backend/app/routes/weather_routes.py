import os
import requests
from flask import Blueprint, jsonify, request
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create a Blueprint for weather related routes
weather_bp = Blueprint("weather_bp", __name__)


@weather_bp.route("/api/weather", methods=["GET"])
def get_weather():
    """
    Endpoint to retrieve real weather data for a given location.

    Example request:
    /api/weather?lat=-37.81&lon=144.96
    """

    # Get query parameters from the request
    lat = request.args.get("lat")
    lon = request.args.get("lon")

    # Check if parameters are missing
    if not lat or not lon:
        return jsonify({
            "error": "lat and lon are required"
        }), 400

    # Validate that parameters are numeric
    try:
        lat = float(lat)
        lon = float(lon)
    except ValueError:
        return jsonify({
            "error": "lat and lon must be valid numbers"
        }), 400

    # Read API key from environment variables
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        return jsonify({
            "error": "Missing OPENWEATHER_API_KEY in environment variables"
        }), 500

    try:
        # Call OpenWeather One Call API 3.0
        url = "https://api.openweathermap.org/data/3.0/onecall"
        params = {
            "lat": lat,
            "lon": lon,
            "appid": api_key,
            "exclude": "minutely,hourly,daily,alerts",
            "units": "metric"
        }

        response = requests.get(url, params=params, timeout=10)

        # Handle HTTP errors from the external API
        if response.status_code != 200:
            return jsonify({
                "error": "Unable to fetch weather data from external API"
            }), 502

        data = response.json()
        current_data = data.get("current", {})

        temperature = current_data.get("temp")
        wind_speed = current_data.get("wind_speed")

        weather_list = current_data.get("weather", [])
        condition = "Unknown"

        if weather_list and isinstance(weather_list, list):
            condition = weather_list[0].get("main", "Unknown")

        if temperature is None or wind_speed is None:
            return jsonify({
                "error": "No weather data available"
            }), 404

        return jsonify({
            "latitude": lat,
            "longitude": lon,
            "temperature": temperature,
            "condition": condition,
            "wind_speed": wind_speed
        }), 200

    except requests.exceptions.Timeout:
        return jsonify({
            "error": "External API request timed out"
        }), 504

    except requests.exceptions.RequestException:
        return jsonify({
            "error": "Unable to fetch weather data"
        }), 500

    except Exception:
        return jsonify({
            "error": "Unexpected server error while processing weather data"
        }), 500