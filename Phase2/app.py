import tkinter as tk
from tkinter import filedialog, Text
import os
import sqlite3

root = tk.Tk()

def addApp():
    #filename = filedialog.askopenfilename(initialdir="/",title="Select a Car Brand", filetypes=(("executables","*.exe"), ("all files","*.*")))
    conn = sqlite3.connect('Phase2.sqlite')
    c = conn.cursor()
    c.execute("SELECT * FROM Brand")


canvas = tk.Canvas(root, height=700,width=500,bg="white")
canvas.pack()

brandBtn = tk.Button(root, text="Select a Car Brand",padx=10,pady=5,fg="black",bg="gray", command=addApp)
brandBtn.pack()

modelBtn = tk.Button(root, text="Select a Car Model",padx=10,pady=5,fg="black",bg="gray")
modelBtn.pack()

extraBtn = tk.Button(root, text="Car Packages",padx=10,pady=5,fg="black",bg="gray")
extraBtn.pack()

root.mainloop()