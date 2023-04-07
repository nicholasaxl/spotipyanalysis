import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id='a57cdc869b44491ebbca0dea632cafe8', client_secret='fb879f29b5514be2b588ba23da47d7f1')
spotify = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

artist_id = 'spotify:artist:7n2Ycct7Beij7Dj7meI4X0'
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
#spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_albums(artist_id, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])


artist_name = 'DPR LIVE'
result = spotify.search(q=artist_name, type='artist')
artist_id = result['artists']['items'][0]['id']

print(artist_id)


results = spotify.artist_top_tracks(artist_id)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    if track['preview_url'] is not None:
        print('audio    : ' + track['preview_url'])
    else:
        print('audio    : Not available')
    print('cover art: ' + track['album']['images'][0]['url'])
    print()

user = 'spotify'
playlists = spotify.user_playlists(user)

for playlist in playlists['items']:
    print(playlist['name'])
    print('  total tracks', playlist['tracks']['total'])


for playlist in playlists['items']:
    print(playlist['name'])
    results = spotify.playlist_tracks(playlist['id'])
    for track in results['items']:
        print(track['track']['name'])
