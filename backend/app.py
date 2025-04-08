from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/generate-quiz', methods=['POST'])
def generate_quiz():
    data = request.get_json()
    topic = data.get('topic')
    difficulty = data.get('difficulty')
    quiz_type = data.get('quiz_type')

    # Dummy quiz data (replace with actual logic)
    quiz = {
        "topic": topic,
        "difficulty": difficulty,
        "quiz_type": quiz_type,
        "questions": [
            {
                "question": f"What is {topic}?",
                "options": ["Option A", "Option B", "Option C", "Option D"],
                "answer": "Option A"
            }
        ]
    }

    return jsonify(quiz)

if __name__ == '__main__':
    app.run(debug=True)

