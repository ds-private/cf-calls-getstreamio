import os


class Config:
    APP_ID = os.environ.get("CALLS_APP_ID", "3dd59331e7a9811a03b4fe2d21140d18")
    APP_SECRET = os.environ.get(
        "CALLS_APP_SECRET",
        "1ea89966a9e2afaee1d03f12955fc597392876597ff9fa8b0785ba942b050c96",
    )
    BASE_PATH = os.environ.get(
        "BASE_PATH",
        "https://rtc.live.cloudflare.com/v1",
        # "https://eo7t07xifmum2qz.m.pipedream.net"
    )
    SOCK_SERVER_OPTIONS = {"ping_interval": 25}
