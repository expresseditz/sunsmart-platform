from flask import Blueprint, jsonify

# Create a Blueprint for health check routes
health_bp = Blueprint("health_bp", __name__)


@health_bp.route("/api/health", methods=["GET"])
def health_check():
    """
    Health check endpoint to verify that the backend server is running.
    This is useful for frontend connectivity checks and monitoring.
    """
    return jsonify({
        "status": "ok",
        "message": "Sun Smart API is running"
    }), 200