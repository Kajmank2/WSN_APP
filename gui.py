import  tkinter as tk
import random

from PIL import ImageTk,Image
def InitGui():
        main_window =tk.Tk()
        scrollbar = tk.Scrollbar(main_window,orient = 'vertical')
        scrollbar.pack(side='right', fill='y')
        #PADY , PADX - PADDINGI

        #Labels POI
#RADIOBuTTONS=======================================================================================
        MODES = [("36",36),("144",144),("411",411)]
        poi=tk.StringVar()
        poi.set(36)
        for text, mode in MODES:
                tk.Radiobutton(main_window,variable=poi, text=text, value=mode,command=lambda : clicked(text)).pack()
#=======================================================



        # RADIO BUTTONS CHANGE POI
        def clicked(value):
                value=poi.get()
                c = tk.Canvas(main_window, width=343, height=343, bg="blue")
                c.pack()
                # ENTRY
                count = tk.StringVar()
                radius = tk.StringVar()
                count.set("0")
                radius.set("0")
                tk.Label(text="COUNT").pack()
                countSens = tk.Entry(main_window,textvariable =count, width=10, borderwidth=5, ).pack()
                tk.Label(text="RADIUS").pack()
                radiusSens = tk.Entry(main_window,textvariable =radius ,width=10, borderwidth=5).pack()



                #VARIABLES FOR STATMENT
                long=10
                longb=5
                i=0
                if (value == "36"):
                        c.destroy()
                        c = tk.Canvas(main_window, width=343, height=343, bg="white")
                        c.create_rectangle(0, 0, 10 , 10, fill="red")
                        c.create_rectangle(66, 0, 76, 10, fill="red")
                        c.pack()
                        for x in range(6):
                                c.create_rectangle(0+i, 0, 0+i+long, 10, fill="red")
                                c.create_rectangle(0+i, 0, 0+i+long, 10, fill="red")
                                c.create_rectangle(0 + i, 66, 0 + i + long, 76, fill="red")
                                c.create_rectangle(0 + i, 133, 0 + i + long, 143, fill="red")
                                c.create_rectangle(0 + i, 199, 0 + i + long, 209, fill="red")
                                c.create_rectangle(0 + i, 265, 0 + i + long, 275, fill="red")
                                c.create_rectangle(0 + i, 331, 0 + i + long, 343, fill="green")
                                i=i+66;



                       # battery = c.create_rectangle(0, 0, 10, 10, fill='red')
                elif (value == "144"):
                        c.destroy()
                        c = tk.Canvas(main_window, width=400, height=400, bg="white")
                        c.pack()
                        for x in range(12):
                                c.create_rectangle(0 + i, 0, 0 + i + longb, 5, fill="red")
                                c.create_rectangle(0 + i, 33, 0 + i + longb, 38, fill="red")
                                c.create_rectangle(0 + i, 66, 0 + i + longb, 71, fill="red")
                                c.create_rectangle(0 + i, 99, 0 + i + longb, 104, fill="red")
                                c.create_rectangle(0 + i, 132, 0 + i + longb, 137, fill="red")
                                c.create_rectangle(0 + i, 165, 0 + i + longb, 170, fill="red")
                                c.create_rectangle(0 + i, 198, 0 + i + longb, 203, fill="green")
                                c.create_rectangle(0 + i, 231, 0 + i + longb, 236, fill="red")
                                c.create_rectangle(0 + i, 264, 0 + i + longb, 269, fill="red")
                                c.create_rectangle(0 + i, 297, 0 + i + longb, 302, fill="green")
                                c.create_rectangle(0 + i, 330, 0 + i + longb, 335, fill="red")
                                c.create_rectangle(0 + i, 363, 0 + i + longb, 365, fill="red")
                                c.create_rectangle(0 + i, 396, 0 + i + longb, 401, fill="green")
                                i = i + 33;
                elif (value == "411"):
                        c.destroy()
                        c = tk.Canvas(main_window, width=400, height=400, bg="white")
                        c.pack()
                        for x in range(20):
                                c.create_rectangle(0 + i, 0, 0 + i + longb, 3, fill="red")
                                c.create_rectangle(0 + i, 20, 0 + i + longb, 23, fill="red")
                                c.create_rectangle(0 + i, 40, 0 + i + longb, 43, fill="red")
                                c.create_rectangle(0 + i, 60, 0 + i + longb, 63, fill="red")
                                c.create_rectangle(0 + i, 80, 0 + i + longb, 83, fill="red")
                                c.create_rectangle(0 + i, 100, 0 + i + longb, 103, fill="red")
                                c.create_rectangle(0 + i, 120, 0 + i + longb, 123, fill="red")
                                c.create_rectangle(0 + i, 140, 0 + i + longb, 143, fill="red")
                                c.create_rectangle(0 + i, 160, 0 + i + longb, 163, fill="red")
                                c.create_rectangle(0 + i, 180, 0 + i + longb, 183, fill="red")
                                c.create_rectangle(0 + i, 200, 0 + i + longb, 203, fill="red")
                                c.create_rectangle(0 + i, 220, 0 + i + longb, 223, fill="red")
                                c.create_rectangle(0 + i, 240, 0 + i + longb, 243, fill="red")
                                c.create_rectangle(0 + i, 260, 0 + i + longb, 263, fill="red")
                                c.create_rectangle(0 + i, 280, 0 + i + longb, 283, fill="red")
                                c.create_rectangle(0 + i, 300, 0 + i + longb, 303, fill="red")
                                c.create_rectangle(0 + i, 320, 0 + i + longb, 323, fill="red")
                                c.create_rectangle(0 + i, 340, 0 + i + longb, 343, fill="red")
                                c.create_rectangle(0 + i, 360, 0 + i + longb, 363, fill="red")
                                c.create_rectangle(0 + i, 380, 0 + i + longb, 383, fill="red")
                                c.create_rectangle(0 + i, 400, 0 + i + longb, 403, fill="red")
                                i = i + 20;

                def Init():
                        for number in range(1, 1+int(count.get())):
                                xval = random.randint(0, 400)
                                yval = random.randint(0, 400)
                                s1 = c.create_oval(xval, yval, xval+int(radius.get()) , yval+int(radius.get()) ,
                                                                             outline="#00bfff", width=2)

                myButton = tk.Button(main_window, text="COMPLIE", command=Init)
                myButton.pack()

       # myButton = tk.Button(main_window, text="COMPLIE", command=lambda: clicked(text))
       # myButton.pack()

        #INSTANCE
        main_window.mainloop()


