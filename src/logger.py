import logging
import sys
from src.settings import LOGGER_NAME, LOGGING_LEVEL, LOGGING_DEST

logging.basicConfig(
    filename=LOGGING_DEST,
    level=LOGGING_LEVEL,
    filemode="a",
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
)

logger = logging.getLogger(LOGGER_NAME)
