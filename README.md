[![PyPi](https://img.shields.io/pypi/v/simple-slack-logger)](https://pypi.org/project/simple-slack-logger/)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![License](https://img.shields.io/pypi/l/simple-slack-logger)](http://www.apache.org/licenses/LICENSE-2.0)
[![Versions](https://img.shields.io/pypi/pyversions/simple-slack-logger)](https://pypi.org/project/simple-slack-logger/)
[![CodeFactor](https://www.codefactor.io/repository/github/gixproject/simple-slack-logger/badge)](https://www.codefactor.io/repository/github/gixproject/simple-slack-logger)

# Simple logging with Slack

It helps you to receive all logs from your Python code in Slack channels
using [webhooks](https://api.slack.com/messaging/webhooks).

Install from PyPi:  
`pip install simple-slack-logger`

or from repository:  
`pip install git+https://github.com/gixproject/simple-slack-logger `

## Usage

### Explicit usage

```python
import logging
from slack_logger import SlackHandler

logger = logging.getLogger(__name__)
handler = SlackHandler(webhook="<YOUR_WEBHOOK>")
logger.addHandler(handler)
logger.error("Something bad happened")
```

### Logging config

```python
"handlers": {
    "slack": {
        "class": "slack_logger.SlackHandler",
        "formatter": "default",
        "level": "WARNING",
        "webhook": "<YOUR_WEBHOOK>",
    },
}
```

### Hint

To catch all exceptions from your Python code you can use this in the main module:

```python
def logging_except_hook(exc_type, exc_value, exc_traceback):
    logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = logging_except_hook
```