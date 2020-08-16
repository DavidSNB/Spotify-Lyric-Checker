import lyricsgenius as genius
import spotify_data_scraper as spotify
import file_finder


api = genius.Genius(
    "mbCzTT54Dpe6luxCvCTT_1hLX49XfvHwVZS-y1o0IZm-EebY7KKNgsrEXmNFkM_h",
    remove_section_headers=True)
imported_song_data = spotify.get_song_data()

if __name__ == "__main__":
    pass
    # initial_import()
    # find_lyrics(imported_song_data)


def find_lyrics(songs, collected=[], count=0):
    not_recognised = []

    for song in songs:  # song = [Track, Artist]
        print("========================")
        genius_song = api.search_song(song[0], song[1])
        if genius_song is None:
            print("Song not found :(")
            not_recognised.append([song[0], song[1]])
        else:
            print("Song found :)")
            collected.append([song[0], song[1], genius_song.lyrics])

    print("\n\n")

    if len(songs) == 0 or count > 4:
        # Do something with not_recognised
        return collected
    else:
        find_lyrics(not_recognised, collected, (count + 1))


def initial_import():
    imported = input(
        "Have you imported your up-to-date spotify data? [y/N]\n").lower()

    if imported == "y":
        print("Yay")
    elif imported == "n" or not imported:
        test = file_finder.get_spotify_file()
        print(test)
    else:
        print("Process Aborted!")
        print("=======================================================")
        print("\n")
        initial_import()


initial_import()

search_value = input("What word / phrase are you searching for? \n").lower()
