# routes/quiz_routes.py
from flask import Blueprint, request, jsonify
from models.ai_model import generate_quiz

quiz_blueprint = Blueprint("quiz", __name__)

@quiz_blueprint.route("/generate-quiz", methods=["POST"])
def generate_quiz_route():
    data = request.get_json()
    topic = data.get("topic")
    difficulty = data.get("difficulty")
    quiz_type = data.get("quiz_type")

    if not topic or not difficulty or not quiz_type:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        quiz = generate_quiz(topic, difficulty, quiz_type)
        return jsonify({"quiz": quiz}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
