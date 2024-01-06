import os

path = ""
filenames = ()

begin_num = "0"
prefix = ""
interval = "1"

MAX_NUMBER_LENGTH = 5

def set_input_values(new_prefix, new_begin_num, new_interval):
    global prefix
    global begin_num
    global interval

    prefix = new_prefix
    begin_num = new_begin_num
    interval = new_interval

def get_filenames(new_path):
    global path
    global filenames
    path = new_path

    all_items = os.listdir(path)

    filenames = [item for item in all_items if os.path.isfile(os.path.join(path, item))]

    filenames.sort(key=lambda filename: os.stat(os.path.join(path, filename)).st_ctime)
    
    return filenames

def rename_files():
    global begin_num

    for filename in filenames:

        file_extension = os.path.splitext(filename)[1]

        new_name = prefix + "0" * (MAX_NUMBER_LENGTH - len(begin_num)) + begin_num + file_extension

        os.rename(os.path.join(path, filename), os.path.join(path, new_name))

        begin_num = str(int(begin_num) + int(interval))
