import random
from tkinter import filedialog

import PIL
from PIL import ImageTk, Image, ImageDraw
import tkinter as tk
import subprocess
import os
import sys


def InitGui():
        main_window =tk.Tk()
        scrollbar = tk.Scrollbar(main_window,orient = 'vertical')
        scrollbar.pack(side='right', fill='y')
        #PADY , PADX - PADDINGI
        ListofNumbers=[]
#RADIOBuTTONS=======================================================================================
        MODES = [("36",36),("144",144),("411",411)]
        poi=tk.StringVar()
        poi.set(36)
        for text, mode in MODES:
                tk.Radiobutton(main_window,variable=poi, text=text, value=mode,command=lambda : clicked(text)).pack()
        # RADIO BUTTONS CHANGE POI
        def clicked(value):
                value=poi.get()
                tk.Label(text="X 0-100").pack(side="bottom")
                tk.Label(text="Y 0-100").pack(side="left")
                c = tk.Canvas(main_window, width=400, height=400, bg="white")
                c.pack(side="left")
                c.create_line(0,400,400,400,fill="black",width=3)
                c.create_line(0, 0, 0, 400, fill="black", width=7)
                '''
                frame1 = tk.Frame(main_window)
                frame1.pack()
                MainWindow = c.create_window(10,10,window=frame1, anchor='nw')

                e1 = tk.Entry(frame1)
                e1.pack()
'''

                #X and Y
                # ENTRY
                count = tk.StringVar()
                radius = tk.StringVar()
                color = tk.StringVar()
                count.set("0")
                radius.set("0")
                color.set("0.")
                tk.Label(text="COUNT").pack()
                countSens = tk.Entry(main_window,textvariable =count, width=10, borderwidth=5, ).pack()
                tk.Label(text="RADIUS").pack()
                radiusSens = tk.Entry(main_window,textvariable =radius ,width=10, borderwidth=5).pack()
                tk.Label(text="% Sensor Activity VALUE: 0-1").pack()
                propabilityEntry = tk.Entry(main_window, textvariable=color, width=10, borderwidth=5).pack()



                #VARIABLES FOR STATMENT
                long=10
                longb=5
                i=0
                if (value == "36"):
                        c.pack()
                        for x in range(6):
                                c.create_rectangle(0+i, 0, 0+i+longb, 5, fill="black")
                                c.create_rectangle(0 + i, 66, 0 + i + longb, 71, fill="black")
                                c.create_rectangle(0 + i, 133, 0 + i + longb, 138, fill="black")
                                c.create_rectangle(0 + i, 199, 0 + i + longb, 204, fill="black")
                                c.create_rectangle(0 + i, 265, 0 + i + longb, 270, fill="black")
                                c.create_rectangle(0 + i, 331, 0 + i + longb, 336, fill="black")
                                i=i+66;



                       # battery = c.create_rectangle(0, 0, 10, 10, fill='red')
                elif (value == "144"):
                        for x in range(12):
                                c.create_rectangle(0 + i, 0, 0 + i + longb, 5, fill="black")
                                c.create_rectangle(0 + i, 33, 0 + i + longb, 38, fill="black")
                                c.create_rectangle(0 + i, 66, 0 + i + longb, 71, fill="black")
                                c.create_rectangle(0 + i, 99, 0 + i + longb, 104, fill="black")
                                c.create_rectangle(0 + i, 132, 0 + i + longb, 137, fill="black")
                                c.create_rectangle(0 + i, 165, 0 + i + longb, 170, fill="black")
                                c.create_rectangle(0 + i, 198, 0 + i + longb, 203, fill="black")
                                c.create_rectangle(0 + i, 231, 0 + i + longb, 236, fill="black")
                                c.create_rectangle(0 + i, 264, 0 + i + longb, 269, fill="black")
                                c.create_rectangle(0 + i, 297, 0 + i + longb, 302, fill="black")
                                c.create_rectangle(0 + i, 330, 0 + i + longb, 335, fill="black")
                                c.create_rectangle(0 + i, 363, 0 + i + longb, 368, fill="black")
                                c.create_rectangle(0 + i, 396, 0 + i + longb, 401, fill="black")
                                i = i + 33;
                elif (value == "411"):
                        for x in range(20):
                                c.create_rectangle(0 + i, 0, 0 + i + longb, 3, fill="black")
                                c.create_rectangle(0 + i, 20, 0 + i + longb, 23, fill="black")
                                c.create_rectangle(0 + i, 40, 0 + i + longb, 43, fill="black")
                                c.create_rectangle(0 + i, 60, 0 + i + longb, 63, fill="black")
                                c.create_rectangle(0 + i, 80, 0 + i + longb, 83, fill="black")
                                c.create_rectangle(0 + i, 100, 0 + i + longb, 103, fill="black")
                                c.create_rectangle(0 + i, 120, 0 + i + longb, 123, fill="black")
                                c.create_rectangle(0 + i, 140, 0 + i + longb, 143, fill="black")
                                c.create_rectangle(0 + i, 160, 0 + i + longb, 163, fill="black")
                                c.create_rectangle(0 + i, 180, 0 + i + longb, 183, fill="black")
                                c.create_rectangle(0 + i, 200, 0 + i + longb, 203, fill="black")
                                c.create_rectangle(0 + i, 220, 0 + i + longb, 223, fill="black")
                                c.create_rectangle(0 + i, 240, 0 + i + longb, 243, fill="black")
                                c.create_rectangle(0 + i, 260, 0 + i + longb, 263, fill="black")
                                c.create_rectangle(0 + i, 280, 0 + i + longb, 283, fill="black")
                                c.create_rectangle(0 + i, 300, 0 + i + longb, 303, fill="black")
                                c.create_rectangle(0 + i, 320, 0 + i + longb, 323, fill="black")
                                c.create_rectangle(0 + i, 340, 0 + i + longb, 343, fill="black")
                                c.create_rectangle(0 + i, 360, 0 + i + longb, 363, fill="black")
                                c.create_rectangle(0 + i, 380, 0 + i + longb, 383, fill="black")
                                c.create_rectangle(0 + i, 400, 0 + i + longb, 403, fill="black")
                                i = i + 20;

                def Init():
                        colores=0
                        #List which save param for
                        CircleList=[]
                        countCIRCLE=int(count.get())
                        colores= float(count.get()) * float(color.get())
                        for colorRed in range (1,1+int(colores)):
                                xval = random.randint(0, 400)
                                yval = random.randint(0, 400)
                                s1 = c.create_oval(xval, yval, xval+int(radius.get())*4 , yval+int(radius.get())*4 , stipple="gray50" ,
                                                                             outline="Green", width=1)
                        for colorGreen in range(1, 1 + countCIRCLE-int(colores)):
                                xval = random.randint(0, 400)
                                yval = random.randint(0, 400)
                                s1 = c.create_oval(xval, yval, xval + int(radius.get())*4, yval + int(radius.get())*4,
                                                   stipple="gray50",
                                                   outline="Red", width=1)
                def Exit():
                        python = sys.executable
                        os.execl(python, python, *sys.argv)

                def SaveImage():
                        x=0

                def donothing():  # HELPER
                        x = 0

                ####################################CZYTAJ PLik ####################################################################################
                def Open(): #SENSOR ID FILE
                        text_file = filedialog.askopenfilename(initialdir="C:/", title="Open TextFile",
                                                               filetypes=(("Text Files", "*.txt"),))
                        text_file = open(text_file, 'r')
                        '''
                        for x in text_file:
                                print(x)
                        '''
                        for x in text_file:
                                ListofNumbers.append(x)
                        ListofNumbers.pop(0)
                        for x in ListofNumbers:
                                print(x)
                        for x in ListofNumbers:
                                xx=x[2:4]
                                yy=x[8:10]
                                print(xx+" "+yy)
                                c.create_oval(int(xx)*4, int(yy)*4,int(xx)*4+10,int(yy)*4+10, fill="green",stipple="gray50",
                                                   outline="Red", width=1)

                menubar = tk.Menu(main_window)
                filemenu = tk.Menu(menubar, tearoff=0)
                filemenu.add_command(label="New", command=donothing)
                filemenu.add_command(label="Open", command=Open)
                filemenu.add_command(label="Save", command=donothing)
                filemenu.add_separator()
                filemenu.add_command(label="Exit", command=main_window.quit)
                menubar.add_cascade(label="File", menu=filemenu)

                myButton = tk.Button(main_window, text="COMPLIE", command=Init)
                myButton.pack()
                ExitButton = tk.Button(main_window,text="EXIT",command=Exit)
                ExitButton.pack(side="right")
                SaveButton=tk.Button(main_window,text="SaveImage",command=SaveImage)
                SaveButton.pack(side="left")

                main_window.config(menu=menubar)
#########################################################################################################################

        #INSTANCE
        main_window.mainloop()


