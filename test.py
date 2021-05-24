from tkinter import *

root = Tk()
root.title("Notepad")
root.geometry("800x600+100+100")

s1 = Scrollbar(root)
s1.pack(side=RIGHT, fill=Y)
# HORIZONTAL Set horizontal scroll bar, the default is the vertical
s2 = Scrollbar(root, orient=HORIZONTAL)
s2.pack(side=BOTTOM, fill=X)

# Create a text box
# Wrap settings do not wrap
textpad = Text(root, width=200, yscrollcommand=s1.set, xscrollcommand=s2.set, wrap='none')
textpad.pack(expand=YES, fill=BOTH)

s1.config(command=textpad.yview)
s2.config(command=textpad.xview)

root.mainloop()