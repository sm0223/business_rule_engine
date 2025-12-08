import logging
from logging import Logger
from logging.handlers import RotatingFileHandler
from typing import Optional

_LOG_FILE = "app.log"

def _configure_root_logger() -> None:
    root = logging.getLogger()
    if root.handlers:
        return  # already configured

    root.setLevel(logging.INFO)
    fmt = logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s - %(message)s", "%Y-%m-%d %H:%M:%S"
    )

    sh = logging.StreamHandler()
    sh.setFormatter(fmt)
    root.addHandler(sh)

    # optional file handler (rotating)
    try:
        fh = RotatingFileHandler(_LOG_FILE, maxBytes=10 * 1024 * 1024, backupCount=5)
        fh.setFormatter(fmt)
        root.addHandler(fh)
    except Exception:
        # ignore file handler failures to avoid breaking startup
        pass

def get_logger(name: Optional[str] = None) -> Logger:
    _configure_root_logger()
    return logging.getLogger(name or __name__)


# python
# from utils.logger import get_logger
# logger = get_logger(__name__)

# example usage inside your function:
# logger.info("Starting policy_rules flow for %s", mpp.id)
# logger.debug("Computed data: %s", data)
# on exception:
# logger.exception("bre_flow failed")
