import spotipy, os
sp = spotipy.Spotify()

# os.environ["SPOTIPY_CLIENT_ID"] = "cd46ec5ba31c4ee69ce89bb8546f1818"              # 'your-spotify-client-id'
# os.environ["SPOTIPY_CLIENT_SECRET"] = "b4118cdd1c844908ad8c3a5096d0d14f"          # 'your-spotify-client-secret'
# os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8888/callback"     # 'your-app-redirect-url'


import spotipy
import sys

spotify = spotipy.Spotify()

if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'Radiohead'

results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
    print(artist['name'], artist['images'][0]['url'])
