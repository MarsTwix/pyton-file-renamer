import tkinter as tk
from tkinter.filedialog import askdirectory

TEXT_INPUT_LABELS = ["Begintekst:", "Beginnummer:", "Interval:"]

labelDir = None
filenameListBox = None

def askDir():
    path = askdirectory(title='Folder selecteren')
    if path and labelDir:
        labelDir.config(text=path)

def setup():
    window = tk.Tk()
    window.geometry("400x400")
    window.title("Bestand hernoemer")
    return window

def renderDirLabel(window, index):
    global labelDir 
    labelDir = tk.Label(window, text="Geen folder geselecteerd", wraplength=400)
    labelDir.grid(row=index, sticky="w")

def renderSelectButtons(window, index):
    tk.Button(window, text="Folder selecteren", command=askDir).grid(row=index, sticky="w")

def renderTextInput(window, index):
    frame = tk.Frame(window)
    for i in range(len(TEXT_INPUT_LABELS)):
        label = tk.Label(frame, text=TEXT_INPUT_LABELS[i])
        label.grid(row=i, column=0, sticky="e")

        textInput = tk.Text(frame, height=1, width=10)
        textInput.insert(tk.END, "0")

        textInput.grid(row=i, column=1, columnspan=2)
    frame.grid(row=index, sticky="w")

def renderConvertButton(window, index):
    tk.Button(window, text="Bestanden omzetten").grid(row=index, sticky="w")

def renderListBox(window, index):
    global filenameListBox
    filenameListBox = tk.Listbox(window)
    filenameListBox.grid(row=index, sticky="w")

RENDER_SEQUENCE = [renderSelectButtons, renderTextInput, renderConvertButton, renderDirLabel, renderListBox]

def render():
    window = setup()

    for i in range(len(RENDER_SEQUENCE)):
        RENDER_SEQUENCE[i](window, i)

    window.mainloop()