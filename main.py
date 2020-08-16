import lyricsgenius as genius
import spotify_data_scraper as spotify
import sys


api = genius.Genius(
    "mbCzTT54Dpe6luxCvCTT_1hLX49XfvHwVZS-y1o0IZm-EebY7KKNgsrEXmNFkM_h",
    remove_section_headers=True)

# imported_song_data = spotify.get_song_data()


def initial_import():
    if spotify.data_present():
        imported = input(
            "Have you imported your up-to-date spotify data? [y/N]\n").lower()

        if imported == "y":
            print("Yay")
        elif imported == "n" or not imported:
            test = spotify.get_spotify_file()
            print(test)
        else:
            print("Process Aborted!")
            print("=======================================================")
            print("\n")
            initial_import()
    else:
        input("You need to import a spotify JSON file! [PRESS ENTER]")
        spotify.get_spotify_file(True)

    find_lyrics(spotify.get_song_data())


def select_function():
    function = input(
        "What would you like to do with your data?\n[A] Find the song based on a lyric")


"""
def find_lyrics(songs, collected=[], count=0):
    not_recognised = []

    total = len(songs)

    song_count = 0
    collected_count = 0

    for song in songs:  # song = [Track, Artist]
        print("========================")

        genius_song = api.search_song(song[0], song[1])

        # genius_song_not_full = api.search_song(song[0], song[1], False)

        # No results found for: '_________' <-- Acceptable
        # Specified song does not have a valid URL with lyrics. Rejecting. <-- Error

        if genius_song is None:
            print("Song not found :(")
            not_recognised.append([song[0], song[1]])
        else:
            print("Song found :)")
            collected.append([song[0], song[1], genius_song.lyrics])
            collected_count += 1

        song_count += 1

        print("Loop Progress: " + str(round(song_count/total * 100)) + "%")
        print("Loop Sucess: " + str(round(collected_count/song_count * 100)) + "%")

    print("\n\n")

    if len(songs) == 0 or count > 20:
        # Do something with not_recognised
        return collected
    else:
        find_lyrics(not_recognised, collected, (count + 1))
"""


def find_lyrics(songs, collected=[], count=0):
    not_recognised = []

    for song in songs:  # song = [Track, Artist]
        song_find_attempts = 0
        genius_song = None

        while not genius_song and song_find_attempts < 5:
            genius_song = api.search_song(song[0], song[1])

            if genius_song is not None:
                collected.append([song[0], song[1], genius_song.lyrics])
            else:
                genius_song = api.search_song(song[0], song[1], False)
                if genius_song is not None:
                    collected.append([song[0], song[1], genius_song.lyrics])

            song_find_attempts += 1

        # No results found for: '_________' <-- Acceptable
        # Specified song does not have a valid URL with lyrics. Rejecting. <-- Error

        if genius_song is None:
            print("Song not found :(")
            not_recognised.append([song[0], song[1]])

    print("\n\n")

    if len(not_recognised) == 0:
        return collected
    elif count > 3:
        # Do something with not_recognised
        return collected
    else:
        find_lyrics(not_recognised, collected, (count + 1))


if __name__ == "__main__":
    initial_import()
    # find_lyrics(imported_song_data)

# search_value = input("What word / phrase are you searching for? \n").lower()
