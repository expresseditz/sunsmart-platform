from flask import Blueprint, jsonify

# Create a Blueprint for awareness related routes
awareness_bp = Blueprint("awareness_bp", __name__)


@awareness_bp.route("/api/awareness", methods=["GET"])
def get_awareness():
    """
    Endpoint to provide static awareness content for Epic 2.
    """

    return jsonify({
        "education_text": [
            "UV levels in Australia can be high even on cool or cloudy days.",
            "Skin damage can occur quickly when the UV Index is 3 or above.",
            "Using sunscreen, hats, and shade helps reduce UV exposure."
        ],
        "skin_type_advice": {
            "fair": "Higher burn risk. Use SPF 50+ and avoid prolonged sun exposure.",
            "medium": "Moderate burn risk. Use sunscreen and seek shade during peak UV.",
            "dark": "Lower burn risk, but UV protection is still recommended."
        },
        "statistics": [
            {
                "label": "Skin cancer cases",
                "value": 12000
            },
            {
                "label": "High UV days",
                "value": 34
            }
        ]
    }), 200