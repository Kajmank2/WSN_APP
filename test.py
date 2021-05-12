import  tkinter as tk
main_window =tk.Tk()


c = tk.Canvas(main_window, width=400, height=400, bg="blue")
c.pack()
i=0
c.create_rectangle(0, 0, 8, 8, fill="red", outline = 'blue')
longb=5
for x in range(12):
    c.create_rectangle(0 + i, 0, 0 + i + longb, 5, fill="red")
    c.create_rectangle(0 + i, 0 + i, 0 + i + longb, i + longb, fill="red")
    c.create_rectangle(0 + i, 0 + i, 0 + i + longb, i + longb, fill="red")
    c.create_rectangle(0 + i, 0 + i, 0 + i + longb, i + longb, fill="red")
    c.create_rectangle(0 + i, 0 + i, 0 + i + longb, i + longb, fill="red")
    c.create_rectangle(0 + i, 0 + i, 0 + i + longb, i + longb, fill="red")
    c.create_rectangle(0 + i, 0 + i, 0 + i + longb, i + longb, fill="green")
    c.create_rectangle(0 + i, 0 + i, 0 + i + longb, i + longb, fill="red")
    c.create_rectangle(0 + i, 0 + i, 0 + i + longb, i + longb, fill="red")
    c.create_rectangle(0 + i, 0 + i, 0 + i + longb, i + longb, fill="green")
    c.create_rectangle(0 + i, 0 + i, 0 + i + longb, i + longb, fill="red")
    c.create_rectangle(0 + i, 0 + i, 0 + i + longb, i + longb, fill="red")
    c.create_rectangle(0 + i, 0 + i, 0 + i + longb, i + longb, fill="green")
    c.create_rectangle(0 + i, 0 + i, 0 + i + longb, i + longb, fill="red")
    c.create_rectangle(0 + i, 0 + i, 0 + i + longb, i + longb, fill="green")
    c.create_rectangle(0 + i, 0 + i, 0 + i + longb, i + longb, fill="red")

    i = i + 33;
main_window.mainloop()