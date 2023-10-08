import os

path = ""
filenames = ()

def get_filenames(new_path):
    global path
    global filenames
    path = new_path

    all_items = os.listdir(path)

    filenames = [item for item in all_items if os.path.isfile(os.path.join(path, item))]
    
    return filenames