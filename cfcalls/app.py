import json

from flask import Flask, jsonify, request
from flask_sock import Sock

from cfcalls.calls_api import CallsApp
from cfcalls.config import Config

app = Flask(__name__)
sock = Sock(app)
app.config.from_object(Config)
calls_app = CallsApp()

TEMP_WS = {}


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


@app.route("/call/default/<call_id>/join", methods=["POST"])
def join(call_id):
    try:
        print("JOIN:", call_id, request.data)
        return jsonify({}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@sock.route("/connect")
def echo(ws):
    while True:
        data = ws.receive()
        print(data)
        TEMP_WS["ws"] = ws

        # After connect is successful
        data = {
            "type": "connection.ok",
            "created_at": "2024-10-15T23:16:30.749093134Z",
            "connection_id": "66f1336c-0a1d-35cb-0200-000001fd1a3d",
            "me": {
                "id": "Boba_Fett",
                "name": "Alamin",
                "image": "https://getstream.io/random_svg/?id=oliver\u0026name=Oliver",
                "custom": {},
                "language": "",
                "role": "user",
                "teams": [],
                "created_at": "2023-07-28T04:27:44.753365Z",
                "updated_at": "2024-10-13T16:12:43.195499Z",
                "banned": False,
                "online": True,
                "devices": [],
                "invisible": False,
                "mutes": [],
                "channel_mutes": [],
                "unread_count": 0,
                "total_unread_count": 0,
                "unread_channels": 0,
                "unread_threads": 0,
            },
        }
        ws.send(json.dumps(data))


if __name__ == "__main__":
    app.run(debug=True)
