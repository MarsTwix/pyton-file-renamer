import os
import gui

path = ""
filenames = []
prefix = ""

MAX_NUMBER_LENGTH = 5

def set_input_values(new_prefix):
    global prefix

    prefix = new_prefix

def get_filenames(new_path):
    global path
    global filenames
    global prefix

    path = new_path

    all_items = os.listdir(path)

    filenames = [f for f in all_items if os.path.isfile(os.path.join(path, f))]

    for filename in filenames:
        if os.path.splitext(filename)[0][-MAX_NUMBER_LENGTH:].isdigit():
            prefix = os.path.splitext(filename)[0][:-MAX_NUMBER_LENGTH]
            break

    filenames.sort(key=lambda filename: os.stat(os.path.join(path, filename)).st_ctime)

    return filenames

def rename_files():

    begin_num = 0
    gui.progressbar.configure(maximum=len(filenames)+0.1)

    for filename in filenames:

        file_extension = os.path.splitext(filename)[1]

        new_name = prefix + "0" * (MAX_NUMBER_LENGTH - len(str(begin_num))) + str(begin_num) + file_extension

        os.rename(path + "/" + filename, path + "/" + new_name,)

        begin_num = begin_num + 1

        gui.progressbar['value'] = begin_num
