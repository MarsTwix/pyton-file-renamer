import tkinter as tk
from tkinter.filedialog import askdirectory, askopenfilenames
import os

window = tk.Tk()

# window.attributes('-fullscreen', True)
window.geometry("500x500")
window.title("Bestand hernoemer")

frame = tk.Frame(master=window)

path = ""
filenames = ()

def askDir():
    path = askdirectory(title='Folder selecteren')
    if path:
        labelDir.config(text=path)
        print(os.listdir(path))

labelDir = tk.Label(frame, text="Geen folder geselecteerd")
buttonDir = tk.Button(frame, text="Folder selecteren", command=askDir)

labelDir.grid(row=0, column=0)
buttonDir.grid(row=0, column=1)

def askFiles():
    filenames = askopenfilenames(title='Bestanden selecteren')
    print(filenames)
    if filenames:
        labelFiles.config(text=filenames)
        print(os.listdir(filenames))

labelFiles = tk.Label(frame, text="Geen bestanden geselecteerd")
buttonFiles = tk.Button(frame, text="Bestanden selecteren", command=askFiles)

labelFiles.grid(row=1, column=0)
buttonFiles.grid(row=1, column=1)

frame.pack()

window.mainloop()
