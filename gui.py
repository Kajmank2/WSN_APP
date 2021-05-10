import  tkinter as tk
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

        #ENTRY
        tk.Label(text="COUNT").pack()
        countSens=tk.Entry(main_window,width =10 , borderwidth=5,).pack()
        tk.Label(text="RADIUS").pack()
        radiusSens=tk.Entry(main_window, width=10, borderwidth=5).pack()


        # RADIO BUTTONS CHANGE POI
        def clicked(value):
                value=poi.get()
                c = tk.Canvas(main_window, width=343, height=343, bg="blue")
                c.pack()
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
                        c = tk.Canvas(main_window, width=400, height=400, bg="blue")
                        c.pack()
                        for x in range(12):
                                c.create_rectangle(0 + i, 0, 0 + i + longb, 5, fill="red")
                                c.create_rectangle(0 + i, 33, 0 + i + longb, 38, fill="red")
                                c.create_rectangle(0 + i, 66, 0 + i + longb, 29, fill="red")
                                c.create_rectangle(0 + i, 99, 0 + i + longb, 41, fill="red")
                                c.create_rectangle(0 + i, 132, 0 + i + longb, 53, fill="red")
                                c.create_rectangle(0 + i, 165, 0 + i + longb, 65, fill="red")
                                c.create_rectangle(0 + i, 198, 0 + i + longb, 77, fill="green")
                                c.create_rectangle(0 + i, 231, 0 + i + longb, 53, fill="red")
                                c.create_rectangle(0 + i, 264, 0 + i + longb, 65, fill="red")
                                c.create_rectangle(0 + i, 72, 0 + i + longb, 77, fill="green")
                                c.create_rectangle(0 + i, 84, 0 + i + longb, 89, fill="red")
                                c.create_rectangle(0 + i, 96, 0 + i + longb, 97, fill="red")
                                c.create_rectangle(0 + i, 108, 0 + i + longb, 113, fill="green")
                                c.create_rectangle(0 + i, 120, 0 + i + longb, 125, fill="red")
                                c.create_rectangle(0 + i, 132, 0 + i + longb, 137, fill="green")
                                c.create_rectangle(0 + i, 144, 0 + i + longb, 149, fill="red")


                                i = i + 33;
                elif (value == "411"):
                        c.destroy()
                        c = tk.Canvas(main_window, width=400, height=400, bg="blue")
                        c.pack()
                        battery = c.create_rectangle(0, 0, 10, 10, fill='yellow')


       # myButton = tk.Button(main_window, text="COMPLIE", command=lambda: clicked(text))
       # myButton.pack()

        #INSTANCE
        main_window.mainloop()


