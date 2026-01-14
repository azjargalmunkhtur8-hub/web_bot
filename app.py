from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")
    try:
        response = requests.post(
            RASA_URL,
            json={"sender": "user1", "message": user_msg}
        )
        bot_reply = response.json()[0]["text"]
    except Exception as e:
        bot_reply = "Rasa server холбогдоогүй байна."
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
