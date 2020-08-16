from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
# show an "Open" dialog box and return the path to the selected file


def get_spotify_file():
    return(askopenfilename(
        initialdir="D:/Downloads",
        title="Select Spotify JSON",
        filetypes=(("JSON", "*.json"), ("All Files", "*.*"))))


"""
from tkinter import *
from tkinter import filedialog

root = Tk()


def get_spotify_file():
    root.filename = filedialog.askopenfilename(
        initialdir="D:/Downloads",
        title="Select Spotify JSON",
        filetypes=(("JSON", "*.json"), ("All Files", "*.*")))

    return root.filename


test = get_spotify_file()
print(test)

root.mainloop()
"""
