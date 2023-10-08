import os

path = ""
filenames = ()

def get_filenames(new_path):
    global path
    global filenames
    path = new_path
    filenames = os.listdir(path)
    return filenames