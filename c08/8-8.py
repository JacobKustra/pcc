def make_album(artist, album, songs=None):
    if songs:
        full_album = {"artist": artist, "album": album, "songs": songs}
    else:
        full_album = {"artist": artist, "album": album}
    print(full_album)

while True:
    print('\nEnter the albumn details:')
    print('Press "q" to quit at anytime')

    artist = input("Enter the artist's name: ")
    if artist == 'q':
        break
    album = input("Enter the album's name: ")
    if album == 'q':
        break
    songs = input("Enter the number of songs: ")
    if songs == 'q':
        break
    
    make_album(artist, album, songs)
