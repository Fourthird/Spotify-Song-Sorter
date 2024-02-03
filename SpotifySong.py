import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id = '7c8f0c578676415db59310fec119001f'
client_secret = '0c84a139779a4e2eb948ec26d42cc68c'
redirect_uri = 'http://localhost:8888/callback'
playlist_id = '5DP1grYsjsxa4aPEiXkGy8'

def get_spotify_tracks(playlist_id):
    # Replace with your Spotify app credentials

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope='playlist-read-private'))

    results = sp.playlist_tracks(playlist_id)

    track_names = []

    while results:
        for item in results['items']:
            track_names.append(item['track']['name'])

        results = sp.next(results)

    return track_names

all_tracks = get_spotify_tracks(playlist_id)

# Writes the songs into the new txt file
file_path = 'SongList.txt'

for track_name in all_tracks:
    with open(file_path, 'a', encoding= 'utf-8') as file:
        file.write(track_name + "\n")

