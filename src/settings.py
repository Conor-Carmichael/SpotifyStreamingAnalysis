import logging


WEEKDAYS = []
SEASONS = []


INPUT_DATA_DIR = "./data/input/gdpr_request_dec_2020/"
DROP_COLS = ["ms_played", "ts", "username", "longitude", "latitude", "episode_name","episode_show_name"]
LOGGER_NAME = "SpotifyAnalyzer"
LOGGING_LEVEL = logging.INFO
LOGGING_DEST = "./data/output/log"
