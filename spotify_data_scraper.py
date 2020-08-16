import json
import io
import os
# from datetime import datetime

spotify_directory = "./spotify_data/"


def read(file_location):
    file = io.open(file_location, "r", encoding="utf8")
    data = json.load(file)
    file.close()
    return data


def get_song_data():
    songs = []
    entry_data = []

    for file in os.listdir(spotify_directory):
        if file.endswith(".json"):
            raw_data = read(spotify_directory + file)

            for entry in raw_data:
                entry_data = [entry["trackName"], entry["artistName"]]
                if entry_data not in songs:
                    songs.append(entry_data)
                else:
                    songs.remove(entry_data)
                    songs.append(entry_data)

    songs.reverse()

    return songs

    # datetime.strptime(string, "%Y-%m-%d %H:%M")


if __name__ == "__main__":
    print(get_song_data())
