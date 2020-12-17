'''

    * The global variables for the project,
        File paths...


'''

import os, sys

# Very clearly, this is poorly done.
# TODO: revise this code to use more dynamic approaches. Wont work when I switch to my laptop
ROOT = os.getcwd()

paths = {
    'base': os.path.join(ROOT),
    'data':  os.path.join(ROOT, 'src', 'data'),
    'ohe':   os.path.join(ROOT, 'src', 'data', 'OHE'),
    'streams_csv' : os.path.join(ROOT, 'src', 'data', 'streams.csv'),
    'extended_gdpr':  os.path.join(ROOT, 'src', 'data', 'extendedGDPR'),
    'gdpr':  os.path.join(ROOT, 'src', 'data', 'baseGDPR'),
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


weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
months   = ['January','February','March','April','May','June','July','August','September','October','November','December']
seasons  = ['Winter','Spring','Summer','Fall']
