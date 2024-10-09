from flask import Flask, jsonify, request

from cfcalls.calls_api import CallsApp
from cfcalls.config import Config

app = Flask(__name__)
app.config.from_object(Config)
calls_app = CallsApp()


@app.route("/calls/sessions/new", methods=["POST"])
def create_new_session():
    try:
        result = calls_app.new_session(request.json)
        return result, 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/calls/sessions/<session_id>/tracks/new", methods=["POST"])
def create_new_tracks(session_id):
    try:
        result = calls_app.new_tracks(request.json, session_id)
        return result, 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/calls/sessions/<session_id>/renegotiate", methods=["PUT"])
def renegotiate(session_id):
    try:
        result = calls_app.renegotiate(request.json, session_id)
        return result, 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
