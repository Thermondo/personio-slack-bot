import os

SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
PERSONIO_CLIENT_ID = os.environ.get("PERSONIO_CLIENT_ID")
PERSONIO_CLIENT_SECRET = os.environ.get("PERSONIO_CLIENT_SECRET")
SENTRY_DSN = os.environ.get("SENTRY_DSN")

PUBLIC_TIME_OFF_TYPES = [
    t.strip() for t in os.environ.get("PUBLIC_TIME_OFF_TYPES", "").split(",")
]


if SENTRY_DSN:
    import sentry_sdk

    sentry_sdk.init(SENTRY_DSN)
