from flask import Blueprint, jsonify
from app.services.uv_service import get_mock_uv_data

uv_bp = Blueprint("uv", __name__)

@uv_bp.route("/api/test", methods=["GET"])
def test():
    return jsonify({
        "message": "backend works"
    })

@uv_bp.route("/api/uv", methods=["GET"])
def get_uv():
    data = get_mock_uv_data()
    return jsonify(data)