import pandas as pd
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.oauth2 as oauth2


def authenticate(user_id, client_secret) -> spotipy.Spotify:
    credentials = oauth2.SpotifyClientCredentials(
        client_id=user_id, client_secret=client_secret
    )
    token = credentials.get_access_token()
    spotify_client = spotipy.Spotify(auth=token)
    return spotify_client


def create_playlist(user: spotipy.Spotify, name: str, df: pd.DataFrame) -> str:

    raise NotImplementedError()
