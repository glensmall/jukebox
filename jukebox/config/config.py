from dotenv import load_dotenv
import os

# class to read and hold the config info from env
class Config(object):

    def __init__(self):

        # load the local .env file so we can grab the data
        load_dotenv()

        self.Client_ID = os.getenv("SPOTIFY_CLIENT_ID")
        self.Client_Secret = os.getenv("SPOTIFY_CLIENT_SECRET")
        self.Redirect_URL = os.getenv("SPOTIFY_REDIRECT_URL")
        self.SpotifyScope = os.getenv("SPOTIFY_SCOPE")
        self.ServerPort = os.getenv("SERVER_PORT")
