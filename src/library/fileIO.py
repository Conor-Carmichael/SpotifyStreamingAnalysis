'''

    Dealing with loading, saving. 
        * Loading the files for processing the JSON files
        * Loading/saving the pickle files
        * Loading the CSV with the stream data
        * Some functions are very simple, but just make it simpler in later pieces.

'''

import os, sys, pickle, json
import pandas as pd
import numpy as np
from src.library.config import paths, ohe_columns, drop_columns

from src.library.general import ohe, transform_ts


#-------------------#
# Pickle functions  #
#-------------------#

def get_ohe_fp(name):
    return os.path.join(paths['ohe'], name)

def save_ohe(store: dict, fp):
    # Use pickle to store the store dict. Returns false on an error in saving
    try:
        with open(fp, 'wb') as store_file:
            pickle.dump(store, store_file)

        return True

    except e as Exception:
        print(e)
        return False

def load_ohe(fp):
    # Use pickle to load in the storage dicts.
    # Returns a blank {} if not exist.
    if os.path.exists(fp):
        with open(fp, 'rb') as store:
            return pickle.load(store)
    else:
        return {}


def load_all_ohe():
    # Returns a dict, the keys are the OHE columns (from the config array)
    # The values are the ohe dicts
    ohe_dict = {}
    for col in ohe_columns:
        fp = get_ohe_fp(col)
        ohe_dict[col] = load_ohe(fp)

    return ohe_dict

#-----------------#
# Data Ingestion  #
#-----------------#

def create_ohe_dicts():
    # First time use, create the OHE dictionaries.
    ohe_dict = {}
    for c in ohe_columns:
        ohe_dict[c] = {}
    return ohe_dict


def clean_json(json_file, ohe_dicts, logging=0):
    for entry in json_file:
        entry['ts'] = transform_ts(entry['ts']) # transform the timestamp into a datetime obj
        # Do one hot encoding on string columns that do not need representation
        for key in ohe_columns:
            entry[key] = ohe(entry[key], ohe_dicts[key])
        
        [entry.pop(key) for key in drop_columns] # Remove the dropped columns

    return json_file


# def handle_jsons


def create_streams_csv(logging=0):
    files = os.listdir(paths['extended_gdpr'])
    stream_logs = list(filter(lambda f: 'endsong' in f, files))
    ohe_dicts = create_ohe_dicts()

    streams_df = pd.DataFrame()
    for f in stream_logs:
        with open(os.path.join(paths['extended_gdpr'], f) , 'r', encoding="UTF-8") as j:
            print(f'Reading {f}....')
            stream_log = json.load(j)
            stream_log_cleaned = clean_json(stream_log, ohe_dicts)
            # print(type(stream_log_cleaned))
            prepped_df = pd.DataFrame.from_dict(stream_log_cleaned)
            streams_df = pd.concat([prepped_df, streams_df], ignore_index=True) if not streams_df.empty else prepped_df


    # Save the one hot encodings 
    print('Saving one hot encoding information...')
    for key in ohe_dicts.keys():
        save_ohe( ohe_dicts[key], get_ohe_fp(key) )

    print('Sorting streams data...')
    streams_df.sort_values(by='ts', inplace=True)
    streams_df.to_csv(paths['streams_csv'])
    print(f"All JSON files have been read and added to a csv, located at {paths['streams_csv']}")


# def sort


def load_streams_df():    
    return pd.read_csv(paths['streams_csv'])



