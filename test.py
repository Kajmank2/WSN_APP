import  tkinter as tk
main_window =tk.Tk()


c = tk.Canvas(main_window, width=400, height=400, bg="blue")
c.pack()
i=0
c.create_rectangle(0, 0, 8, 8, fill="red", outline = 'blue')
longb=5
for x in range(12):
    c.create_rectangle(0 + i, 0, 0 + i + longb, 5, fill="red")
    c.create_rectangle(0 + i, 12, 0 + i + longb, 17, fill="red")
    c.create_rectangle(0 + i, 24, 0 + i + longb, 29, fill="red")
    c.create_rectangle(0 + i, 36, 0 + i + longb, 41, fill="red")
    c.create_rectangle(0 + i, 48, 0 + i + longb, 53, fill="red")
    c.create_rectangle(0 + i, 60, 0 + i + longb, 65, fill="red")
    c.create_rectangle(0 + i, 72, 0 + i + longb, 77, fill="green")
    c.create_rectangle(0 + i, 48, 0 + i + longb, 53, fill="red")
    c.create_rectangle(0 + i, 60, 0 + i + longb, 65, fill="red")
    c.create_rectangle(0 + i, 72, 0 + i + longb, 77, fill="green")
    c.create_rectangle(0 + i, 84, 0 + i + longb, 89, fill="red")
    c.create_rectangle(0 + i, 96, 0 + i + longb, 97, fill="red")
    c.create_rectangle(0 + i, 108, 0 + i + longb, 113, fill="green")
    c.create_rectangle(0 + i, 120, 0 + i + longb, 125, fill="red")
    c.create_rectangle(0 + i, 132, 0 + i + longb, 137, fill="green")
    c.create_rectangle(0 + i, 144, 0 + i + longb, 149, fill="red")

    i = i + 33;
main_window.mainloop()