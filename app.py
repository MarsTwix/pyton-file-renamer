import tkinter as tk
from tkinter.filedialog import askdirectory, askopenfilenames
import os

window = tk.Tk()
window.geometry("500x500")
window.title("Bestand hernoemer")

frame = tk.Frame(master=window)

dirLabelFrame = tk.Frame(master=frame)
selectButtonFrame = tk.Frame(master=frame)
textInputFrame = tk.Frame(master=frame)

path = ""
filenames = ()

textInputLabels = ["Begintekst", "Beginnummer", "Interval"]

def askDir():
    path = askdirectory(title='Folder selecteren')
    if path:
        labelDir.config(text=path)
        print(os.listdir(path))

labelDir = tk.Label(dirLabelFrame, text="Geen folder geselecteerd", wraplength=400)
buttonDir = tk.Button(selectButtonFrame, text="Folder selecteren", command=askDir)

listBox = tk.Listbox(window)

def askFiles():
    filenames = askopenfilenames(title='Bestanden selecteren')
    if filenames:
        for filename in filenames:
            listBox.insert(tk.END, filename)

buttonFiles = tk.Button(selectButtonFrame, text="Bestanden selecteren", command=askFiles)

convertButton = tk.Button(window, text="Bestanden omzetten")

labelDir.grid(row=0, column=0)
dirLabelFrame.grid(row=0)

buttonDir.grid(row=0, column=0)
buttonFiles.grid(row=0, column=1)
selectButtonFrame.grid(row=1)

for i in range(len(textInputLabels)):
    label = tk.Label(textInputFrame, text=textInputLabels[i])
    label.grid(row=i, column=0, sticky="e")

    textInput = tk.Text(textInputFrame, height=1, width=10)
    textInput.grid(row=i, column=1, columnspan=2)
textInputFrame.grid(row=2)

convertButton.grid(row=1, column=0)
listBox.grid(row=2, column=0)

frame.grid(row=0, sticky="w")

window.mainloop()