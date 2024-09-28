from cfcalls.calls_api import CallsApp
from cfcalls.config import Config
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config.from_object(Config)
calls_app = CallsApp(app.config["APP_ID"], app.config["BASE_PATH"])

@app.route("/new_session", methods=["POST"])
def create_new_session():
    data = request.json
    offer_sdp = data.get("offer_sdp")
    try:
        result = calls_app.new_session(offer_sdp)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/new_tracks", methods=["POST"])
def create_new_tracks():
    data = request.json
    track_objects = data.get("track_objects")
    offer_sdp = data.get("offer_sdp", None)
    try:
        result = calls_app.new_tracks(track_objects, offer_sdp)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/send_answer", methods=["PUT"])
def send_answer_sdp():
    data = request.json
    answer_sdp = data.get("answer_sdp")
    try:
        calls_app.send_answer_sdp(answer_sdp)
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)