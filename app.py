import tkinter as tk
from tkinter.filedialog import askdirectory, askopenfilenames
import os

window = tk.Tk()

# window.attributes('-fullscreen', True)
window.geometry("500x500")
window.title("Bestand hernoemer")

frame = tk.Frame(master=window)
textInputFrame = tk.Frame(master=window)

path = ""
filenames = ()

textInputLabels = ["Begintekst", "Beginnummer", "Interval"]

def askDir():
    path = askdirectory(title='Folder selecteren')
    if path:
        labelDir.config(text=path)
        print(os.listdir(path))

labelDir = tk.Label(frame, text="Geen folder geselecteerd")
buttonDir = tk.Button(frame, text="Folder selecteren", command=askDir)

labelDir.grid(row=0, column=0)
buttonDir.grid(row=0, column=1)

listBox = tk.Listbox(frame)

def askFiles():
    filenames = askopenfilenames(title='Bestanden selecteren')
    if filenames:
        for filename in filenames:
            listBox.insert(tk.END, filename)

buttonFiles = tk.Button(frame, text="Bestanden selecteren", command=askFiles)

buttonFiles.grid(row=1, column=1)

listBox.grid(row=1, column=0)

for i in range(len(textInputLabels)):
    label = tk.Label(textInputFrame, text=textInputLabels[i])
    label.grid(row=i, column=0, sticky="e")

    textInput = tk.Text(textInputFrame, height=1, width=10)
    textInput.grid(row=i, column=1, columnspan=2)

frame.grid()

textInputFrame.grid()

window.mainloop()
