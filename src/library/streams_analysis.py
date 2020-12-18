'''

    File holds all functions for collecting information on the dataframe.


'''

# from src.library.config import weekdays, months, seasons
import src.library.config as cfg 


def get_window(df, col, start, end):
    # From start, through end.
    assert end > =start, "Error in start, end args. Start is greater than end value."

    if start == end:
        return df[ (df[col] == start) ]
    else:
        return df[ (df[col] >= start) & (df[col] < end) ]


# def filter_by(df, col, )


def get_weekday(df, day:str):

    assert day.title() in cfg.weekdays or day.lower() == 'all', \
    f"day argument must be 'all' or one of the following, {str(weekdays)}"

    return df[ df['date'].weekday() == day ]


def get_first_n_listens(df, col:str, name:str, n=10):
    # Assumes df is sorted, as that is how I store it.
    return None


def apply_listen_length_threshold(df, threshold:float, key='secPlayed'):
    assert threshold > 0, "Threshold less than or equal to 0."
    assert df[key].max() > threshold , f"Threshold value must be less than the max listen length in the dataframe, {max_thresh}"
    
    return df[ (df[key ] >= threshold) ]

    
def stats_by_track(df, skip_thresh=30):
    '''
        Gets unique combinations of songs/artists (in case of the same song name across two artists),
        Tracks the following stats across the artists: 
            ['track', 'artist', 'streams', 'skips, 'avgTimePerPlay', 'first_play']
        Using skip threshold to determine what a skip is. Total time includes "skips"
    '''

    no_duplicates = df[['artistName','trackName']].drop_duplicates()
    length = len(no_duplicates)
    print(f"Length of track/artist pairs: {length}")

    tracks, artists = no_duplicates['trackName'].values, no_duplicates['artistName'].values
    ####
    assert len(tracks) == len(artists)
    ####
    new_columns = ['track', 'artist', 'streams', 'skips', 'totalTime', 'avgSecPlayed', 'mostFreqWeekday', 'firstPlay']

    results = []
    d = len(tracks)
    for i, (artist, track) in enumerate(zip(artists, tracks)):
        clear_output(wait=True)
        print(f"Pair {i} of {length}\n\t{track} by {artist}")
        obs = df[ (df['trackName'] == track) & (df['artistName'] == artist)] # All the observations of this song/artist pair in the dataframe

        times = obs['secPlayed'].values 
        dates = obs['date'].values #np array of datetime date objs
        weekday_vals = [d.weekday() for d in dates] 

        total_time = sum(times)
        streams = len(obs)
        sorted_dates = sorted(dates)
        entry = {
            'track': track, 
            'artist': artist,
            'streams': streams,
            'skips': (times > skip_thresh).sum(),
            'totalTime': total_time,
            'avgSecPlayed':  total_time/streams,
            'mostFreqWeekday': stats.mode(weekday_vals),
            'firstPlay': sorted_dates[0]
        }


        results.append(entry)
    
    return pd.DataFrame(data=results, columns=new_columns)

def stats_by_artist(df, skip_thresh=30):
    '''
        Gets unique artists 
        Tracks the following stats across the artists: 
            ['artist', 'uniqueTracks', 'streams', 'skips, 'avgTimePerPlay', 'first_play']
        Using skip threshold to determine what a skip is. Total time includes "skips"
    '''
    artists = df['artistName'].unique()

    new_columns = ['artist', 'uniqueTracks', 'streams', 'skips', 'totalTime', 'avgSecPlayed', 'mostFreqWeekday', 'firstPlay']

    results = []
    d = len(artists)
    for i, artist in enumerate(artists):
        clear_output(wait=True)
        print(f"Artist {i} of {d}\n\t{artist}")
        obs = df[df['artistName'] == artist] # All the observations of this song/artist pair in the dataframe

        times = obs['secPlayed'].values 
        dates = obs['date'].values #np array of datetime date objs
        weekday_vals = [d.weekday() for d in dates] # Look above for how I get thsi should I even store this though?

        total_time = sum(times)
        streams = len(obs)

        entry = {
            'artist': artist,
            'uniqueTracks': len(obs['trackName'].unique()),
            'streams':streams,
            'skips': (times > skip_thresh).sum(),
            'totalTime': total_time,
            'avgSecPlayed':  total_time/streams,
            'mostFreqWeekday': stats.mode(weekday_vals),
            'firstPlay': sorted(dates)[0]
        }

        results.append(entry)
    
    return pd.DataFrame(data=results, columns=new_columns)