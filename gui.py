import tkinter as tk
from tkinter.filedialog import askdirectory
import converter

TEXT_INPUT_LABELS = [
    {"label": "Begintekst:", "value": "", "textbox": None}, 
    {"label": "Beginnummer:", "value": "0", "textbox": None}, 
    {"label": "Interval:", "value": "1", "textbox": None}
]

label_dir = None
filename_list_box = None

def ask_dir():
    path = askdirectory(initialdir="./", title='Folder selecteren')
    if path and label_dir:
        filenames = converter.get_filenames(path)

        label_dir.config(text=path)

        filename_list_box.delete(0, tk.END)

        for filename in filenames:
            filename_list_box.insert(tk.END, filename)

def convert_files():

    converter.set_input_values(
        TEXT_INPUT_LABELS[0]["textbox"].get("1.0", 'end-1c'),
        TEXT_INPUT_LABELS[1]["textbox"].get("1.0", 'end-1c'),
        TEXT_INPUT_LABELS[2]["textbox"].get("1.0", 'end-1c')
    )

    converter.rename_files()

    TEXT_INPUT_LABELS[1]["textbox"].delete("1.0", tk.END)
    TEXT_INPUT_LABELS[1]["textbox"].insert(tk.END, converter.begin_num)

    filenames = converter.get_filenames(converter.path)

    filename_list_box.delete(0, tk.END)

    for filename in filenames:
        filename_list_box.insert(tk.END, filename)

def setup():
    window = tk.Tk()
    window.geometry("400x400")
    window.title("Bestand hernoemer")
    return window

def render_dir_label(window, index):
    global label_dir 
    label_dir = tk.Label(window, text="Geen folder geselecteerd", wraplength=400)
    label_dir.grid(row=index, sticky="w")

def render_select_buttons(window, index):
    tk.Button(window, text="Folder selecteren", command=ask_dir).grid(row=index, sticky="w")

def render_text_input(window, index):
    frame = tk.Frame(window)
    for i in range(len(TEXT_INPUT_LABELS)):
        label = tk.Label(frame, text=TEXT_INPUT_LABELS[i]["label"])
        label.grid(row=i, column=0, sticky="e")

        TEXT_INPUT_LABELS[i]["textbox"] = tk.Text(frame, height=1, width=10)
        TEXT_INPUT_LABELS[i]["textbox"].insert(tk.END, TEXT_INPUT_LABELS[i]["value"])

        TEXT_INPUT_LABELS[i]["textbox"].grid(row=i, column=1, columnspan=2)
    frame.grid(row=index, sticky="w")

def render_convert_button(window, index):
    tk.Button(window, command=convert_files, text="Bestanden omzetten").grid(row=index, sticky="w")

def render_list_box(window, index):
    global filename_list_box

    frame = tk.Frame(window)

    filename_list_box = tk.Listbox(frame)
    filename_list_box.grid(row=index, sticky="w")

    scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
    scrollbar.grid(row=index, column=1, sticky="ns")

    filename_list_box.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=filename_list_box.yview)

    frame.grid(row=index, sticky="w")

RENDER_SEQUENCE = [render_select_buttons, render_text_input, render_convert_button, render_dir_label, render_list_box]

def render():
    window = setup()

    for i in range(len(RENDER_SEQUENCE)):
        RENDER_SEQUENCE[i](window, i)

    window.mainloop()
