'''

    File holds general functions for the proejct.

'''
import json
from datetime import datetime

def transform_ts(ts):
    # Time stampts are in coordinated universal time. May want to convert to local time.
    return datetime.strptime(ts, '%Y-%m-%dT%H:%M:%SZ')


def transform_ms_played(data):
    ms = float(data['ms_played'])
    return ms/1000


def ohe(value:str, store:dict):
    # Essentially does one hot encoding for the values in the dataframe by column.
    # Useful for some columns, not to be used where the name is really important. Just to reduce memory space.
    if value in store:
        return store[value]
    else:
        store[value] = len(store)
        return store[value]


'''
    Functions for interfacing with Spotipy.
'''

def create_playlist(df_sect):
    return None


def login(creds):
    return None