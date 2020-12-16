'''

    * The global variables for the project,
        File paths...


'''

import os, sys

# Very clearly, this is poorly done.
# TODO: revise this code to use more dynamic approaches. Wont work when I switch to my laptop
paths = {
    'base': os.path.join('D:\Conor Carmichael\code\SpotifyGDPRAnalyzer'),
    'data':  os.path.join('D:\Conor Carmichael\code\SpotifyGDPRAnalyzer\src\data'),
    'ohe':  os.path.join('D:\Conor Carmichael\code\SpotifyGDPRAnalyzer\src\data\OHE'),
    'streams_csv' : os.path.join('D:\Conor Carmichael\code\SpotifyGDPRAnalyzer\src\data\streams.csv'),
    'extended_gdpr': os.path.join('D:\Conor Carmichael\code\SpotifyGDPRAnalyzer\src\data\extendedGDPR'),
    'gdpr': os.path.join('D:\Conor Carmichael\code\SpotifyGDPRAnalyzer\src\data\extendedGDPR'),
}

ohe_columns = [
    'platform',
    'conn_country',
    'ip_addr_decrypted',
    'reason_start',
    'reason_end',
    'episode_show_name'
]



drop_columns = [
    'username',
    'episode_name',
    'episode_show_name',
    'city',
    'region',
    'metro_code',
    'longitude',
    'latitude'
]


keep_columns = []