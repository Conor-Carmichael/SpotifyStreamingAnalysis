import pandas as pd
from src.logger import logger
from src.utils import split_endtime, convert_ms, get_streaming_file_paths
from src.settings import DROP_COLS


class StreamHistory:

    """
    Class to represent stream log files, handles ingestion, preprocessing and cleaning.
    """

    def __init__(
        self,
        data_paths: str,
    ) -> None:
        self.data_paths = data_paths

        self._initalize()

    def _initalize(self):
        # Take in data
        logger.info(f"Loading {self.data_paths}")
        data = pd.concat([pd.read_json(f) for f in self.data_paths])
        self.username = data['username'].values[0]
        ## Clean/process values ##
        # Change date storage type
        apply_fn = lambda row: split_endtime(row["ts"])

        result = data.apply(apply_fn, axis=1, result_type="expand")
        data = pd.concat([data, result], axis="columns")

        # Use seconds not ms
        data["seconds_played"] = data["ms_played"].apply(lambda s: convert_ms(s))
        data["skipped"] = data["skipped"].apply(lambda v: True if v > 0 else False)

        self.start_date = data["date"].min()
        self.end_date = data["date"].max()

        data = data.sort_values(by=["date", "time"], ascending=False)

        data = data.drop(DROP_COLS, axis=1)

        self.data = data
        self.stream_count = len(data)
        self.time_streamed = self.data['seconds_played'].sum()
        logger.info(f"Total streams: {self.stream_count}")


stream_history = StreamHistory(data_paths=[f for f in get_streaming_file_paths()])
