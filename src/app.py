import datetime
from re import S
import src.utils as utils
from src.stream_log import stream_history

import streamlit as st



date_range_start = st.date_input(
    "Start",
    value=stream_history.start_date,
    min_value=stream_history.start_date,
    max_value=stream_history.end_date,
)
date_range_end = st.date_input(
    "End",
    value=stream_history.end_date,
    min_value=stream_history.start_date,
    max_value=stream_history.end_date,
)

windowed_data = utils.get_window(stream_history.data, start=date_range_start, end=date_range_end)
st.dataframe(windowed_data)

stream_count, time_listened, top_track, top_artist = st.columns(4)
stream_count.metric("Total Streams", len(windowed_data))
time_listened.metric("Time Listened", str(datetime.timedelta(seconds=windowed_data['seconds_played'].sum()) ))
top_track.metric("Most Played Track", windowed_data.mode()['master_metadata_track_name'][0])
top_artist.metric("Most Played Artist", windowed_data.mode()['master_metadata_album_artist_name'][0])

show_time_listened_over_time = st.checkbox("Show time streaming trend chart")

if show_time_listened_over_time:
    st.altair_chart(utils.get_time_listened_plot(windowed_data))