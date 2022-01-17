import datetime
from re import S
import src.utils as utils
from src.settings import *
from src.stream_log import stream_history
from itertools import compress
import streamlit as st

st.title(f"Stream Insights for {stream_history.username}")

# st.multiselect
date_range_col, season_col, weekday_col, country_col = st.columns(4)
with date_range_col:
    st.header("Filter for streams by date range")
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
with season_col:
    st.header("Filter for streams by season")
    seasonal_filters = [st.checkbox(s) for s in SEASONS.keys()]
with weekday_col:
    st.header("Filter for streams by day of the week")
    weekday_filters = [st.checkbox(w) for w in WEEKDAYS]
with country_col:
    st.header("Filter for streams by country streamed from")
    country_filters = [st.checkbox(cc) for cc in stream_history.data['conn_country'].unique()]


processed_data = utils.get_window(stream_history.data, start=date_range_start, end=date_range_end)
if any(seasonal_filters):
    processed_data = utils.season_filter(processed_data, list(compress(SEASONS.keys(), seasonal_filters)) )

if any(weekday_filters):
    processed_data = utils.weekday_filter(processed_data, list(compress(WEEKDAYS, weekday_filters)) )

if any(country_filters):
    processed_data = processed_data[ processed_data['conn_country'].apply(lambda c : c in country_filters) ]

time_played_filter = st.slider("Minimum play time to consider", value=5.0, min_value=0.0, max_value=100.0)
len_before_time_filter = len(processed_data)
processed_data = processed_data[ processed_data['seconds_played'] >= time_played_filter ]
streams_omitted_by_time = len_before_time_filter - len(processed_data)
st.text(f"Time filter drops {streams_omitted_by_time} rows")

# Metric display
stream_count, time_listened, top_track, top_artist = st.columns(4)
stream_count.metric("Total Streams", len(processed_data))
time_listened.metric("Time Listened", str(datetime.timedelta(seconds=processed_data['seconds_played'].sum()) ))
top_track.metric("Most Played Track", processed_data.mode()['master_metadata_track_name'][0])
top_artist.metric("Most Played Artist", processed_data.mode()['master_metadata_album_artist_name'][0])

st.dataframe(processed_data[COL_ORDERING(list(processed_data.columns))])


show_time_listened_over_time = st.checkbox("Show time streaming trend chart")
if show_time_listened_over_time:
    st.altair_chart(utils.get_time_listened_plot(processed_data))


hist_dropdown = st.selectbox("Histogram value", ['Artist','Track','Album'])
st.altair_chart(utils.get_histogram(processed_data, {"Track": 'master_metadata_track_name', 'Artist': 'master_metadata_album_artist_name', 'Album': 'master_metadata_album_album_name'}[hist_dropdown]))