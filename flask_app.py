from flask import Flask, render_template, request, jsonify, send_file
from src.helper2 import llm_model, text_to_speech
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify(
            success=False,
            message="No text received from client"
        ), 400

    user_text = data["text"].strip()

    if user_text == "":
        return jsonify(
            success=False,
            message="Empty query received"
        ), 400

    response = llm_model(user_text)

    if not response or response.strip() == "":
        return jsonify(
            success=False,
            message="Model did not return any response"
        ), 500


    audio_file = text_to_speech(response)

    return jsonify(
        success=True,
        question=user_text,
        answer=response,
        audio_file=audio_file
    )


@app.route("/audio/<filename>")
def audio(filename):
    audio_path = os.path.join("audio", filename)

    if not os.path.exists(audio_path):
        return jsonify(
            success=False,
            message="Audio file not found"
        ), 404

    return send_file(audio_path, mimetype="audio/mpeg")


if __name__ == "__main__":
    app.run(debug=True)
