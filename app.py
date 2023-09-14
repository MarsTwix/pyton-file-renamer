import tkinter as tk
from tkinter.filedialog import askdirectory
import os

window = tk.Tk()

# window.attributes('-fullscreen', True)
window.geometry("500x500")
window.title("File renamer")

frame = tk.Frame(master=window)

path = ""

def askDir():
    path = askdirectory(title='Folder selecteren')
    if path:
        label.config(text=path)
        print(os.listdir(path))
        

label = tk.Label(frame, text="Geen folder geselecteerd")
button = tk.Button(frame, text="Folder selecteren", command=askDir)

label.grid(row=0, column=0)
button.grid(row=0, column=1)

frame.pack()

window.mainloop()
