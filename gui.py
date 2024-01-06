import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter import ttk
import converter

prefix_input = None
label_dir = None
filename_list_box = None

progress = None

def ask_dir():
    path = askdirectory(initialdir="./", title='Folder selecteren')
    if path and label_dir:
        filenames = converter.get_filenames(path)

        prefix_input.delete("1.0", tk.END)
        prefix_input.insert(tk.END, converter.prefix)

        label_dir.config(text=path)

        filename_list_box.delete(0, tk.END)

        for filename in filenames:
            filename_list_box.insert(tk.END, filename)

def convert_files():

    converter.set_input_values(
        prefix_input.get("1.0", 'end-1c'),
    )

    converter.rename_files()

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
    global prefix_input

    frame = tk.Frame(window)

    label = tk.Label(frame, text="Begintekst:")
    label.grid(row=0, column=0, sticky="e")

    prefix_input = tk.Text(frame, height=1, width=10)
    prefix_input.insert(tk.END, "")

    prefix_input.grid(row=0, column=1, columnspan=2)
    frame.grid(row=index, sticky="w")

def render_convert_button(window, index):
    tk.Button(window, command=convert_files, text="Bestanden omzetten").grid(row=index, sticky="w")

def render_progressbar(window, index):
    global progressbar

    progressbar = ttk.Progressbar(window, orient=tk.HORIZONTAL, length=160)
    progressbar.grid(row=index, sticky="w")

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

RENDER_SEQUENCE = [render_select_buttons, render_text_input, render_convert_button, render_progressbar, render_dir_label, render_list_box]

def render():
    window = setup()

    for i in range(len(RENDER_SEQUENCE)):
        RENDER_SEQUENCE[i](window, i)

    window.mainloop()
