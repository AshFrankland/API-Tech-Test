import requests
import json
import musicbrainzngs

def get_songs(artist_name):
    musicbrainzngs.set_useragent('lyrics calculator', 'Python')
    artist_search = musicbrainzngs.search_artists(artist_name)
    artist_id = artist_search['artist-list'][0]['id']
    artist_info = musicbrainzngs.get_artist_by_id(artist_id, includes=['recordings'])
    song_list = []
    for song in range(5):
        song_list.append(artist_info['artist']['recording-list'][song]['title'])
    return song_list

def get_lyrics(artist_name, song_title):
    request = requests.get('https://api.lyrics.ovh/v1/' + artist_name + '/' + song_title)
    response_body = json.loads(request.content)
    if 'lyrics' not in response_body.keys():
        return False
    lyrics = response_body['lyrics']
    return lyrics

def main():
    artist_name = input('Select an Artist: ')

    song_list = get_songs(artist_name)

    space_count = 0
    song_count = 0

    for song_title in song_list:
        lyrics = get_lyrics(artist_name, song_title)
        if lyrics:
            space_count += lyrics.count(' ')
            song_count += 1

    if song_count == 0:
        print('No songs/lyrics could be found, sorry')
    else:
        average_lyrics = space_count//song_count
        print('\nThe average number of lyrics in a song by {} is {}'.format(artist_name, average_lyrics))

if __name__ == '__main__':
    main()