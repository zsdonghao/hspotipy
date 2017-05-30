import spotipy, os
import spotipy.util as util
"""
http://spotipy.readthedocs.io/en/latest/#authorized-requests

https://github.com/plamere/spotipy/tree/master/examples
"""

def main_non_auth():
    ## Non-Authorized requests
    name = 'ladygaga'
    spotify = spotipy.Spotify()
    results = spotify.search(q='artist:' + name, type='artist')
    print(results)

def main_auth_code_flow():
    ## Authorization Code flow
    os.environ["SPOTIPY_CLIENT_ID"] = "cd46ec5ba31c4ee69ce89bb8546f1818"              # 'your-spotify-client-id'
    os.environ["SPOTIPY_CLIENT_SECRET"] = "b4118cdd1c844908ad8c3a5096d0d14f"          # 'your-spotify-client-secret'
    os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8888/callback"     # 'your-app-redirect-url'

    scope = 'user-library-read'

    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Usage: %s username" % (sys.argv[0],))
        sys.exit()

    token = util.prompt_for_user_token(username, scope)

    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_saved_tracks()
        for item in results['items']:
            track = item['track']
            print(track['name'] + ' - ' + track['artists'][0]['name'])
    else:
        print("Can't get token for", username)

def main_client_credentials_flow(arg):
    ## Client Credentials Flow
    # https://github.com/plamere/spotipy/blob/master/examples/client_credentials_flow.py
    # from spotipy.oauth2 import SpotifyClientCredentials
    #
    # client_credentials_manager = SpotifyClientCredentials()
    # sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    #
    # playlists = sp.user_playlists('spotify')
    # while playlists:
    #     for i, playlist in enumerate(playlists['items']):
    #         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    #     if playlists['next']:
    #         playlists = sp.next(playlists)
    #     else:
    #         playlists = None

    from spotipy.oauth2 import SpotifyClientCredentials
    import spotipy
    import pprint

    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    search_str = 'Muse'
    result = sp.search(search_str)
    pprint.pprint(result)


if __name__ == '__main__':
    main_non_auth()
    # main_auth_code_flow()
    # main_client_credentials_flow()
