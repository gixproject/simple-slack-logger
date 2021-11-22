import logging

import requests

__version__ = "0.6.0"


class SlackHandler(logging.Handler):
    """
    Logging handler to send messages to a Slack via webhook.
    """

    COLORS = {
        "CRITICAL": "danger",
        "ERROR": "danger",
        "WARN": "warning",
        "WARNING": "warning",
        "INFO": "good",
    }

    def __init__(self, webhook: str):
        super(SlackHandler, self).__init__()
        self.webhook = webhook

    def emit(self, record):
        attachments = {
            "fallback": f"Incoming {record.levelname.lower()} log",
            "title": "Incoming log",
            "text": record.message if hasattr(record, "message") else record.msg,
            "footer": record.levelname,
            "ts": record.created,
            "color": self.COLORS.get(record.levelname, self.COLORS["WARNING"]),
            "fields": [
                {
                    "title": "Module path",
                    "value": f"{record.pathname}:{record.lineno}",
                    "short": False,
                },
            ],
        }

        if record.exc_text:
            attachments["fields"].append({"title": "Traceback", "value": record.exc_text, "short": False})
        if record.args and len(record.args) < 10:
            attachments["fields"].append({"title": "Arguments", "value": str(record.args), "short": False})

        try:
            requests.post(url=self.webhook, json={"attachments": [attachments]})
        except:
            self.handleError(record)
