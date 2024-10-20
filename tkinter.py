import tkinter as tk
root = tk.Tk()
root.title ("TK intro")
root.geometry("500x500")
textLabel = tk.Label(root,text="My name is Deborah")
textLabel.pack()
entry = tk.Entry(root)
entry.pack()
def sayHelloFunction():
    x = entry.get()
    print("Hello!!!!!!!!!!!!!!!!",x)
sayHello = tk.Button(root,bg = "green",fg = "white",text = "sayHello!!!",command =sayHelloFunction, relief = "solid")
sayHello.pack()
root.mainloop()