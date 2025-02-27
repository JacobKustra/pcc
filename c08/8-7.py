def make_album(artist, album, songs=None):
    if songs:
        full_album = {"artist": artist, "album": album, "songs": songs}
    else:
        full_album = {"artist": artist, "album": album}
    print(full_album)

make_album("Eminem", "Encore")
make_album("Soul", "Hey")
make_album("Train", "Test")
make_album("Rain", "Man", 12)
