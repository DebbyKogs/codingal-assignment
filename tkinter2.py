import tkinter as tk
from tkinter import Label, PhotoImage, font
tkinterObject = tk.Tk()
tkinterObject.geometry("500x500")
tkinterObject.configure(bg="red")
tkinterObject.title("Title")
frame1 = tk.Frame(tkinterObject, bg="black", borderwidth=6, relief="sunken", padx=50)
frame1.pack(side="left", fill="y")
label = tk.Label(frame1, text="Welcome to codingal", bg="purple", fg="white", padx=10, pady=10)
label.pack(pady=10)
frame2 = ""
tkinterObject.mainloop()