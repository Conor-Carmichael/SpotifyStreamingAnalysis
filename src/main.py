from src.utils import *
from src.stream_log import StreamHistory
from logger import logger

if __name__ == "__main__":

    files = get_streaming_file_paths()

    sh_0 = StreamHistory(data_path=files[0])
