from flask import Flask, session, render_template
from flask_session import Session
from config import Config
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import uuid

# some globals
cfg = Config()
client = spotipy()

# deifne the global that is the flask APP
app = Flask(__name__)
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = './.flask_session/'
Session(app)

caches_folder = './.spotify_caches/'
if not os.path.exists(caches_folder):
    os.makedirs(caches_folder)

def session_cache_path():
    return caches_folder + session.get('uuid')


# define the default reoute for this app
@app.route('/')
def hello():
    return("This is the default route")


# called to authneticate against the Spotify auth service
@app.route('/login')
def login():

    
   # client = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cfg.ClientID,
                                               client_secret=cfg.ClientSecret,
                                               redirect_uri=cfg.RedirectURL,
                                               scope=cfg.SpotifyScope))

    return()

###########################################
# the main entry point for this application
###########################################
if __name__ == "__main__":

	app.run(threaded=True, port=int(cfg.ServerPort))