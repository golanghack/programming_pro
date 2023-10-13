#! /usr/bin/env python3 

import lyricsgenius as lg

message_for_user: str = 'Enter a filename -> '

# output file for record 
filename: str = input(message_for_user) or 'lyrics.txt'

file = open(filename, 'w+', encoding='utf-8')

# APIGenius 
# token dont save in code!
# never into Accsess Token in code
genius = lg.Genius(
    'zzT-tAg8pFO2D-yhK-YHEK59IxC5IRmdU7vALpOYJMjiVdV3PfnKA0A2tBYOPZTD',
    # skipping sing listing
    skip_non_songs = True,
    # have same lyrics
    excluded_terms = ['(Remix)', '(Live)'],
    # order to keep headers
    remove_section_headers = True
)

# Maximum songs list
message_for_user = 'Enter name of artists separated by spaces -> '
input_string = input(message_for_user)
artist = input_string.split(' ') or input_string.split(" ")

def get_lyrics(arr: list, max_song: int) -> None:
    """get_lyrics return number of songs grabbed by function.
    Saves -> text file with lyrics.
    arr -> Artist
    max_song -> maximum songs to be grabbed
    """
    
    # write lyrics in arr 
    counter = 0
    
    for name in arr:
        try:
            songs = (genius.search_artist(name, max_songs=max_song, sort='popularity')).songs
            song_list = [song.lyrics for song in songs]
            
            # delimeter
            file.write('\n\n <|end-->of-->text|> \n\n'.join(song_list))
            counter += 1
            
            print(f'Songs grabbed -> {len(song_list)}')
            file.close()
        except ValueError as err:
            print(f'Some exception at {name} -> {song_list} -> {err}')


if __name__ == '__main__':
    get_lyrics(artist, 3)
    