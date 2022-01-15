'''
    Author: Conor Carmichael

'''

from datetime import datetime
from typing import *
import pandas as pd
import os

from src.settings import (
    INPUT_DATA_DIR
)

def get_window(df:pd.DataFrame, start:datetime, end: datetime, search_col:str="ts", inclusive:bool=False):
    ''' Get streams [start, end) dates. search_col="ts" '''
    assert start < end, "Start date must be before end date"
    return df[ (df[search_col] >= start) & (df[search_col] < end)]

def convert_ms(time):
    return time / 1000

def get_streaming_file_paths() -> List[str]:
    files = [f for f in os.listdir(INPUT_DATA_DIR) if f.startswith("endsong") and f.endswith(".json")]
    return [os.path.join(INPUT_DATA_DIR, f) for f in files]


def split_endtime(endtime:str):
    ''' Returns datetime object for date, and time seperately (in order) '''
    date_time = endtime.split(" ")
    date, time = date_time[0], date_time[1]
    
    date_obj = datetime.date(*[int(v) for v in date.split("-")])
    time_obj = datetime.date(*[int(v) for v in time.split(":")])

    return {"date": date_obj, "time": time_obj}