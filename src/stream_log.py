import pandas as pd
import datetime

from src.utils import (
    split_endtime,
    convert_ms
)

class StreamHistory:

    '''
    Class to represent a single stream logging file, handles ingestion, preprocessing and cleaning.
    '''

    def __init__(self, data_path:str, ) -> None:
        self.start_date = ""
        self.end_date = ""
        self.data_path = data_path


    def _initalize(self):
        # Take in data
        data = pd.read_json(self.data_path)

        # Clean/process values

        # Change date storage type
        result = data['endTime'].apply(
            lambda endtime: pd.Series(**split_endtime(endtime)),
            result_type="expand"
        )
        data = pd.concat([data, result], axis='columns')

        data['secondsPlayed'] = data['msPlayed'].apply(lambda s: convert_ms(s))
    