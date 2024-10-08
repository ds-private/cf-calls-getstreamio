import requests
from flask import current_app


class CallsApp:
    def __init__(self, app_id, base_path):
        self.prefix_path = f"{base_path}/apps/{app_id}"
        self.session_id = None

    def send_request(self, url, body, method="POST"):
        headers = {
            "content-type": "application/json",
            "Authorization": f'Bearer {current_app.config["APP_SECRET"]}',
        }
        print(f"{self.session_id}, body, url, headers")
        response = requests.request(method, url, json=body, headers=headers)
        print(response.content, response)
        # response.raise_for_status()
        return response.json()

    def check_errors(self, result, tracks_count=0):
        if "errorCode" in result:
            raise ValueError(result["errorDescription"])
        for i in range(tracks_count):
            if "errorCode" in result["tracks"][i]:
                raise ValueError(
                    f'tracks[{i}]: {result["tracks"][i]["errorDescription"]}'
                )

    def new_session(self, offer_sdp):
        url = f"{self.prefix_path}/sessions/new"
        body = {"sessionDescription": {"type": "offer", "sdp": offer_sdp}}
        result = self.send_request(url, body)
        self.check_errors(result)
        self.session_id = result["sessionId"]
        return result

    def new_tracks(self, track_objects, offer_sdp=None):
        url = f"{self.prefix_path}/sessions/{self.session_id}/tracks/new"
        body = {
            "sessionDescription": {"type": "offer", "sdp": offer_sdp},
            "tracks": track_objects,
        }
        if not offer_sdp:
            body.pop("sessionDescription", None)
        result = self.send_request(url, body)
        self.check_errors(result, len(track_objects))
        return result

    def send_answer_sdp(self, answer):
        url = f"{self.prefix_path}/sessions/{self.session_id}/renegotiate"
        body = {"sessionDescription": {"type": "answer", "sdp": answer}}
        result = self.send_request(url, body, method="PUT")
        self.check_errors(result)
