import requests

from cfcalls.config import Config


class CallsApp:
    def __init__(self):
        self.prefix_path = f"{Config.BASE_PATH}/apps/{Config.APP_ID}"

    def send_request(self, url, body, method="POST"):
        headers = {
            "content-type": "application/json",
            "Authorization": f"Bearer {Config.APP_SECRET}",
        }
        response = requests.request(method, url, json=body, headers=headers)
        return response.content

    def new_session(self, data):
        url = f"{self.prefix_path}/sessions/new"
        return self.send_request(url, data)

    def new_tracks(self, data, session_id):
        url = f"{self.prefix_path}/sessions/{session_id}/tracks/new"
        return self.send_request(url, data)

    def renegotiate(self, data, session_id):
        url = f"{self.prefix_path}/sessions/{session_id}/renegotiate"
        return self.send_request(url, data, method="PUT")
