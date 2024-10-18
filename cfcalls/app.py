import json

from flask import Flask, jsonify, request
from flask_sock import Sock

from cfcalls.calls_api import CallsApp
from cfcalls.config import Config

TEMP_WS = {}
app = Flask(__name__)
app.config.from_object(Config)
sock = Sock(app)
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


@app.route("/call/default/<call_id>/join", methods=["POST"])
def join(call_id):
    try:
        print("JOIN:", call_id, request.data)
        data = {
            "type": "call.session_participant_joined",
            "created_at": "2024-10-16T04:15:01.911604755Z",
            "call_cid": "default:lsAVy6CSeqdF",
            "session_id": "0c8c7bec-ecee-4ab6-90e1-1a5989a3e7e4",
            "participant": {
                "user": {
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
                    "blocked_user_ids": [],
                },
                "user_session_id": "aff08503-92ae-4f8c-a4d0-7da90a85b3cc",
                "role": "user",
                "joined_at": "2024-10-16T04:15:01.911590159Z",
            },
        }
        ws = TEMP_WS["ws"]
        ws.send(json.dumps(data))
        data = {
            "call": {
                "type": "default",
                "id": "lsAVy6CSeqdF",
                "cid": "default:lsAVy6CSeqdF",
                "current_session_id": "0c8c7bec-ecee-4ab6-90e1-1a5989a3e7e4",
                "created_by": {
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
                    "blocked_user_ids": [],
                },
                "custom": {},
                "created_at": "2024-10-15T22:48:45.888445Z",
                "updated_at": "2024-10-15T22:48:45.888445Z",
                "recording": False,
                "transcribing": False,
                "ended_at": None,
                "starts_at": None,
                "backstage": False,
                "settings": {
                    "audio": {
                        "access_request_enabled": True,
                        "opus_dtx_enabled": True,
                        "redundant_coding_enabled": True,
                        "mic_default_on": True,
                        "speaker_default_on": True,
                        "default_device": "earpiece",
                        "noise_cancellation": {"mode": "auto-on"},
                    },
                    "backstage": {"enabled": False},
                    "broadcasting": {
                        "enabled": True,
                        "hls": {
                            "auto_on": False,
                            "enabled": True,
                            "quality_tracks": ["720p"],
                        },
                        # "rtmp": {"enabled": True, "quality": "720p"},
                    },
                    "geofencing": {"names": []},
                    "recording": {
                        "audio_only": False,
                        "mode": "available",
                        "quality": "720p",
                    },
                    "ring": {
                        "incoming_call_timeout_ms": 15000,
                        "auto_cancel_timeout_ms": 15000,
                        "missed_call_timeout_ms": 15000,
                    },
                    "screensharing": {
                        "enabled": True,
                        "access_request_enabled": True,
                        "target_resolution": None,
                    },
                    "transcription": {
                        "mode": "available",
                        "closed_caption_mode": "available",
                        "languages": [],
                    },
                    "video": {
                        "enabled": True,
                        "access_request_enabled": True,
                        "target_resolution": {
                            "width": 1280,
                            "height": 720,
                            "bitrate": 1200000,
                        },
                        "camera_default_on": True,
                        "camera_facing": "front",
                    },
                    "thumbnails": {"enabled": False},
                    "limits": {"max_participants": None, "max_duration_seconds": None},
                },
                "blocked_user_ids": [],
                # "ingress": {
                #     "rtmp": {
                #         "address": "rtmps://ingress.stream-io-video.com:443/mmhfdzb5evj2.default.lsAVy6CSeqdF"
                #     }
                # },
                "session": {
                    "id": "0c8c7bec-ecee-4ab6-90e1-1a5989a3e7e4",
                    "started_at": "2024-10-16T04:13:43.007351Z",
                    "ended_at": None,
                    "participants": [],
                    "participants_count_by_role": {"user": 1},
                    "anonymous_participant_count": 0,
                    "rejected_by": {},
                    "accepted_by": {},
                    "missed_by": {},
                    "live_started_at": "2024-10-16T04:13:43.008879Z",
                    "live_ended_at": None,
                    "timer_ends_at": None,
                },
                "egress": {"broadcasting": False, "hls": None, "rtmps": []},
                "thumbnails": None,
                "join_ahead_time_seconds": 0,
            },
            "members": [],
            "membership": None,
            "own_capabilities": [
                "block-users",
                "change-max-duration",
                "create-call",
                "create-reaction",
                "enable-noise-cancellation",
                "end-call",
                "join-call",
                "join-ended-call",
                "mute-users",
                "pin-for-everyone",
                "read-call",
                "remove-call-member",
                "screenshare",
                "send-audio",
                "send-video",
                "start-broadcast-call",
                "start-record-call",
                "start-transcription-call",
                "stop-broadcast-call",
                "stop-record-call",
                "stop-transcription-call",
                "update-call",
                "update-call-member",
                "update-call-permissions",
                "update-call-settings",
            ],
            "blocked_users": [],
            "created": False,
            "credentials": {
                "server": {
                    # "edge_name": "sfu-63b101084fd8.aws-mum1.stream-io-video.com",
                    "edge_name": "localhost:5000",
                    # "url": "https://sfu-63b101084fd8.aws-mum1.stream-io-video.com/twirp",
                    "url": "http://localhost:5000/twirp",
                    # "ws_endpoint": "wss://sfu-63b101084fd8.aws-mum1.stream-io-video.com/ws",
                    "ws_endpoint": "ws://localhost:5000/sfu_ws",
                },
                "token": "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhZTlmZThjMThkN2M4ZWM2ZDczMGYwOWNjZWNkZmUzNyIsInN1YiI6InVzZXIvQm9iYV9GZXR0IiwiYXVkIjpbInNmdS02M2IxMDEwODRmZDguYXdzLW11bTEuc3RyZWFtLWlvLXZpZGVvLmNvbSJdLCJleHAiOjE3MjkwNzM3MDEsIm5iZiI6MTcyOTA1MjEwMSwiaWF0IjoxNzI5MDUyMTAxLCJhcHBfaWQiOjEyNTc1NDUsImNhbGxfaWQiOiJkZWZhdWx0OmxzQVZ5NkNTZXFkRiIsInVzZXIiOnsiaWQiOiJCb2JhX0ZldHQiLCJuYW1lIjoiQWxhbWluIiwiaW1hZ2UiOiJodHRwczovL2dldHN0cmVhbS5pby9yYW5kb21fc3ZnLz9pZD1vbGl2ZXJcdTAwMjZuYW1lPU9saXZlciIsInRwIjoiRHd6T1JNWS81NCt0cjVWQXR6YXpGOUY3R0g5RDJoVFEiLCJ0c2lkIjoicjhpU21aQkhmZGt3cmcreTdsMytBdyJ9LCJyb2xlcyI6WyJ1c2VyIl0sIm93bmVyIjp0cnVlfQ.1-iOZc_RuYPYEFdjvdGnqjBZ3szlVgNDhQkMoohon6YE57yrwQqlagTGrDFJQAvwjVn2MfKS0ssJ2lsvDy2Ovg",
                "ice_servers": [
                    {
                        "urls": ["stun:stun.l.google.com:19302"],
                        "username": "",
                        "password": "",
                    },
                    # TODO: Aditionally pass Cloudflare's TRUN details here:
                    # https://developers.cloudflare.com/calls/turn/generate-credentials/ 
                ],
            },
            "stats_options": {"reporting_interval_ms": 10000},
            "duration": "212.57ms",
        }
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@sock.route("/connect")
def connect(ws):
    while True:
        data = ws.receive()
        print("connect", data)
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


@sock.route("/sfu_ws")
def sfu_ws(ws):
    while True:
        data = ws.receive()
        print("sfu_ws", data)


if __name__ == "__main__":
    app.run(debug=True)
