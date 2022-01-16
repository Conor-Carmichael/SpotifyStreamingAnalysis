"""
    Author: Conor Carmichael

"""

from datetime import datetime
from typing import *
import pandas as pd
import os
import altair as alt

from src.settings import INPUT_DATA_DIR


def get_window(
    df: pd.DataFrame,
    start: datetime,
    end: datetime,
    search_col: str = "date",
    inclusive: bool = False,
):
    '''Get streams [start, end) dates. search_col="ts"'''
    if start <= end:
        return df[(df[search_col] >= start) & (df[search_col] <= end)]

    else:
        return df


def convert_ms(time):
    return time / 1000


def get_streaming_file_paths() -> List[str]:
    files = [
        f
        for f in os.listdir(INPUT_DATA_DIR)
        if f.startswith("endsong") and f.endswith(".json")
    ]
    return [os.path.join(INPUT_DATA_DIR, f) for f in files]


def split_endtime(endtime: str):
    """Returns datetime object for date, and time seperately (in order)"""
    # date_time = endtime[:-1].replace("T"," ")split("T")
    datetime_repr = datetime.strptime(endtime, "%Y-%m-%dT%H:%M:%SZ")

    # date, time = date_time[0], date_time[1][:-1] # ignore trailing z

    # date_obj = datetime.date date.split("-"))
    # time_obj = datetime.time(*time.split(":"))
    return {"date": datetime_repr.date(), "time": datetime_repr.time()}


def get_time_listened_plot(df):

    df['day_total_streaming_time'] = df.apply(lambda row: df[ df['date'] == row['date'] ]['seconds_played'].sum()/60, axis=1)
    
    chart = alt.Chart(df[["day_total_streaming_time", "date"]]).mark_line().encode(
        x=alt.X('date', title="Date"),
        y=alt.Y('day_total_streaming_time', title='Time (minutes)'),
        tooltip=['date','day_total_streaming_time']
    ).properties(title="Time Listened in Date Range").interactive()

    return chart 