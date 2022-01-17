import logging
import os
import numpy as np

WEEKDAYS = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
MONTHS = ["january","february","march","april","may","june","july","august","september","october","november","december"]
SEASONS = {
    "winter":["december","january","february"],
    "spring":["march","april","may"],
    "summer":["june","july","august"],
    "fall":["september","october","november"]
}


INPUT_DATA_DIR = "./data/input/gdpr_request_dec_2020/"
DROP_COLS = ["city", "incognito_mode", "ip_addr_decrypted", "metro_code","offline","offline_timestamp","region","user_agent_decrypted", "ms_played", "ts", "username", "longitude", "latitude", "episode_name","episode_show_name"]

COL_ORDERING = lambda cols: np.unique(['date', 'time', 'master_metadata_track_name', 'master_metadata_album_artist_name'] + cols)

LOGGER_NAME = "SpotifyAnalyzer"
LOGGING_LEVEL = logging.INFO
LOGGING_DEST = "./data/output/log"
