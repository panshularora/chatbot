from flask import Flask, render_template, request, jsonify
from nlp_utils import ensure_model, predict_emotion

app = Flask(__name__, template_folder="templates", static_folder="static")

# Ensure model exists (trains if missing)
ensure_model()


def generate_bot_reply(message: str, emotion: str) -> str:
    responses = {
        "happy": "I'm glad to hear you're feeling good! 😊",
        "sad": "I'm sorry you're feeling down. I'm here if you want to talk.",
        "angry": "I get that this is frustrating. Want to share more?",
        "fear": "That sounds worrying. I'm here with you.",
        "surprise": "Wow, that is unexpected! Tell me more.",
        "love": "That's wonderful to hear! ❤️",
        "neutral": "Thanks for sharing. How can I help today?",
    }
    return responses.get(emotion, "I'm here for you!")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    user_message = (data or {}).get("message", "").strip()
    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    emotion = predict_emotion(user_message)
    reply = generate_bot_reply(user_message, emotion)
    return jsonify({"reply": reply, "emotion": emotion})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


