import lyricsgenius as genius
import spotify_data_scraper as spotify
import sys
import time


api = genius.Genius(
    "mbCzTT54Dpe6luxCvCTT_1hLX49XfvHwVZS-y1o0IZm-EebY7KKNgsrEXmNFkM_h",
    remove_section_headers=True)

collected_songs = []
not_genius = []
matching_songs = []


def quit():
    print("Closing Program...")
    time.sleep(3)
    sys.exit()


def initial_import():
    if spotify.data_present():
        imported = input(
            "Have you imported your up-to-date spotify data? [y/N]\n").lower()

        if imported == "y":
            print("Continuing...")
            imported_properly = True
        elif imported == "n" or not imported:
            imported_properly = spotify.get_spotify_file()
        else:
            print("Unknown Input\n")
            initial_import()
    else:
        input("You need to import a spotify JSON file! [PRESS ENTER]")
        imported_properly = spotify.get_spotify_file(True)

    if not imported_properly:
        resolved_input = False

        while not resolved_input:
            proceed = input(
                "You did not import a file, do you still want to continue? [Y/n]\n").lower()
            if proceed == "y" or not proceed:
                continue
            elif proceed == "m":
                quit()
            else:
                print("Unknown Input\n")

    select_function()


def select_function():
    function = input(
        "What would you like to do with your data?\n[A] Find the song based on a lyric\n[q] Nothing\n").lower()

    if function == "a" or not function:
        lyric_search()
    elif function == "q":
        quit()
    else:
        print("Unknown Input\n")
        select_function()


"""
def find_lyrics(songs, collected_songs=[], count=0):
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


def collect_lyrics(songs=spotify.get_song_data()):
    # collected_songs = []
    # not_genius = []
    if collected_songs == [] and not_genius == []:
        for song in songs:  # song = [Track, Artist]
            song_find_attempts = 1
            genius_song = None

            while not genius_song:
                print("============ ATTEMPT " +
                      str(song_find_attempts) + " ============")

                genius_song = api.search_song(song[0], song[1])
                if genius_song == "None_found":
                    not_genius.append([song[0], song[1]])
                elif genius_song is not None:
                    collected_songs.append(
                        [song[0], song[1], genius_song.lyrics])
                else:
                    song_find_attempts += 1
    else:
        print("Songs already found")
    print("\n\n")
    # return [collected_songs, not_genius]


def lyric_search():
    matching_songs.clear()
    search_lyric = input("What is the lyric you are looking for?\n").lower()

    collect_lyrics()

    for song in collected_songs:
        if search_lyric in song[2].lower():
            matching_songs.append(song)

    for song in matching_songs:
        print("================================================")
        print(song[0] + " by " + song[1])
    print("================================================")


if __name__ == "__main__":
    initial_import()

# search_value = input("What word / phrase are you searching for? \n").lower()
