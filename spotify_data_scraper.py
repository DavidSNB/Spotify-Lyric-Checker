import json
import io
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import shutil
import sys

Tk().withdraw()
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
                if entry["trackName"] != "Unknown Track" or entry["artistName"] != "Unknown Artist":
                    entry_data = [entry["trackName"], entry["artistName"]]
                    if entry_data not in songs:
                        songs.append(entry_data)
                    else:
                        songs.remove(entry_data)
                        songs.append(entry_data)
            print("IMPORTED: " + spotify_directory + file)

    songs.reverse()

    return songs

    # datetime.strptime(string, "%Y-%m-%d %H:%M")


def get_spotify_file(fresh=False):
    file_location = askopenfilename(
        initialdir="D:/Downloads",
        title="Select Spotify JSON",
        filetypes=(("JSON", "*.json"), ("All Files", "*.*")))

    if file_location != '':
        if not fresh:
            resolved_input = False

            while not resolved_input:
                remove_old = input(
                    "Do you want to remove pre-existing files? [y/N]\n").lower()
                if remove_old == "y":
                    for file in os.listdir(spotify_directory):
                        os.remove(spotify_directory + file)
                    print("Files removed.\n")
                    resolved_input = True
                elif remove_old == "n" or not remove_old:
                    print("Files not removed.\n")
                    resolved_input = True
                else:
                    print("Unknown Input\n")

        resolved_input = False

        while not resolved_input:
            copy_or_move = input(
                "Do you want to copy or move the selected file? [C/m]\n").lower()
            if copy_or_move == "c" or not copy_or_move:
                shutil.copy(file_location, spotify_directory)
                print("Files Copied.\n")
                resolved_input = True
            elif copy_or_move == "m":
                shutil.move(file_location, spotify_directory)
                print("Files Moved.\n")
                resolved_input = True

            else:
                print("Unknown Input\n")

        return True
    else:
        return False


def data_present():
    if not os.listdir(spotify_directory):
        return False
    else:
        return True


if __name__ == "__main__":
    print(get_spotify_file())
    # print(get_song_data())
