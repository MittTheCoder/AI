import tkinter as tk
from DrawingPad import DrawingPad
from Brain import Brain

Brain.packBrainModel("model.json")

tk_app = tk.Tk()                          
canvas = DrawingPad(tk_app)
tk_app.title("Machine Learning Drawing Pad")


tk_app.mainloop()