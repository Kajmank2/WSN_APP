import random
from tkinter import filedialog
import PIL
from PIL import ImageTk, Image, ImageDraw
import tkinter as tk
import subprocess
import os
import sys

#LIST TO FILES
s="#id x y"
listSenss = []
ListXySensCov=[]
ListSensorneigh=[]
ListCover=[]
calcSensorID=[]
calcSensorID.append(s)
listSenss.append(s)
SquareArenas=160000/4
amountReadWSN=0
def InitGui():
        main_window =tk.Tk()
        scrollbar = tk.Scrollbar(main_window,orient = 'vertical')
        scrollbar.pack(side='right', fill='y')
        #PADY , PADX - PADDINGI
        ListofNumbers=[]
        ListofNeighbour=[]
        tk.Label(text="X 0-100").pack(side="bottom")
        tk.Label(text="Y 0-100").pack(side="left")
        c = tk.Canvas(main_window, width=400, height=400, bg="white")
        c.pack(side="left")
        c.create_line(0,400,400,400,fill="black",width=3)
        c.create_line(0, 0, 0, 400, fill="black", width=3)
        #POI 411
        #FIRST POI
        def OpenMYSensorStates(): #SENSOR ID FILE
                        text_file = filedialog.askopenfilename(initialdir="C:/", title="Open TextFile",
                                                               filetypes=(("Text Files", "*.txt"),))
                        text_file = open(text_file, 'r')
                        for x in text_file:
                                listSenss.append(x)
                        for x in listSenss:
                                print(x)
                        listSenss.pop(0)
                        for x in listSenss:
                                xx=x[2:4]
                                yy=x[7:9]
                                id=x[0]
                                state=x[12]
                                if state=='0':
                                        colo="red"
                                else:
                                        colo="green"
                                c.create_oval(int(xx) * 4, int(yy) * 4, int(xx) * 4 - 2, int(yy) * 4 + 2,
                                              stipple="gray50",
                                              fill="black", tags=id)
                                c.create_oval(int(xx) * 4 + int(radius.get()) * 4,
                                              int(yy) * 4 + int(radius.get()) * 4,
                                              int(xx) * 4 - int(radius.get()) * 4,
                                              int(yy) * 4 - int(radius.get()) * 4,
                                              stipple="gray50",
                                              outline=colo)
                                c.create_text(int(xx)*4 + 8,
                                              int(yy)*4 + 8,
                                              font="Times 10 italic bold", text=id)
        def OpenSensorWSN():
                        text_file = filedialog.askopenfilename(initialdir="C:/", title="Open TextFile",
                                                               filetypes=(("Text Files", "*.txt"),))
                        text_file = open(text_file, 'r')
                        # DELETE FIRST PARAMETER
                        for x in text_file:
                                ListofNumbers.append(x)
                        ListofNumbers.pop(0)
                        for x in ListofNumbers:
                                print(x)
        longb=5
        i=0
        for x in range(20):
                c.create_rectangle(0 + i, 0, 0 + i + longb, 2, fill="black")
                c.create_rectangle(0 + i, 20, 0 + i + longb, 22, fill="black")
                c.create_rectangle(0 + i, 40, 0 + i + longb, 42, fill="black")
                c.create_rectangle(0 + i, 60, 0 + i + longb, 62, fill="black")
                c.create_rectangle(0 + i, 80, 0 + i + longb, 82, fill="black")
                c.create_rectangle(0 + i, 100, 0 + i + longb, 102, fill="black")
                c.create_rectangle(0 + i, 120, 0 + i + longb, 122, fill="black")
                c.create_rectangle(0 + i, 140, 0 + i + longb, 142, fill="black")
                c.create_rectangle(0 + i, 160, 0 + i + longb, 162, fill="black")
                c.create_rectangle(0 + i, 180, 0 + i + longb, 182, fill="black")
                c.create_rectangle(0 + i, 200, 0 + i + longb, 202, fill="black")
                c.create_rectangle(0 + i, 220, 0 + i + longb, 222, fill="black")
                c.create_rectangle(0 + i, 240, 0 + i + longb, 242, fill="black")
                c.create_rectangle(0 + i, 260, 0 + i + longb, 262, fill="black")
                c.create_rectangle(0 + i, 280, 0 + i + longb, 282, fill="black")
                c.create_rectangle(0 + i, 300, 0 + i + longb, 302, fill="black")
                c.create_rectangle(0 + i, 320, 0 + i + longb, 322, fill="black")
                c.create_rectangle(0 + i, 340, 0 + i + longb, 342, fill="black")
                c.create_rectangle(0 + i, 360, 0 + i + longb, 362, fill="black")
                c.create_rectangle(0 + i, 380, 0 + i + longb, 382, fill="black")
                c.create_rectangle(0 + i, 400, 0 + i + longb, 402, fill="black")
                i = i + 20

                #X and Y
                # ENTRY
        radius = tk.StringVar()
        color = tk.StringVar()
        battery = tk.StringVar()
        radius.set("35")
        color.set("0.5")
        battery.set("10")
                ######################################RADIO BUTTONS##################
        variableRadio = tk.StringVar(main_window, "36")
        def choice(text):
                variableRadio.set(text)
        valuesRadioPOI = {"POI 36": "36", "POI 144":"144", " POI 411" : "411"}
        variableRadio=tk.StringVar(main_window,"36")
        tk.Label(text="---Points of interests (POIs)---").pack()
        for (text, value) in valuesRadioPOI.items():
                        tk.Radiobutton(main_window, text=text, variable=variableRadio,
                                    value=value ,command=choice(value)).pack(ipady=5)
############ RIGHT GUI#########################
        tk.Label(text="---Sensor Parameters---").pack()
        SaveButton = tk.Button(main_window, text="Read WSN", command=OpenSensorWSN).pack()
        tk.Label(text="RADIUS").pack()
        radiusSens = tk.Entry(main_window,textvariable =radius ,width=10, borderwidth=5).pack()
        tk.Label(text="Battery Capacity").pack()
        batteryCapacity = tk.Entry(main_window, textvariable=battery, width=10, borderwidth=5).pack()
        tk.Label(text="---ACTIVE Sensor---").pack()
        tk.Label(text="Probabilistic").pack()
        SaveButton = tk.Button(main_window, text="Read WSN ON/OFF", command=OpenMYSensorStates).pack()
        tk.Label(text="Randomly % Sensor Activity VALUE: 0-1").pack()
        propabilityEntry = tk.Entry(main_window, textvariable=color, width=10, borderwidth=5).pack()
# INICJACJA
        def Init():
                c.delete('all')
                sensorId=0
                listSens= []
                amountReadWSN=0
                #List which save param for
                for x in ListofNumbers:
                    print(x)
                    amountReadWSN = amountReadWSN + 1
                countCIRCLE=amountReadWSN
                colores= float(amountReadWSN) * float(color.get())
                # COLOR FOR CIRCLE
                id = 1
                calcSensorID.clear()
                calcSensorID.append("#id x y")
                for x in ListofNumbers:
                    rand = random.uniform(0, 1)
                    if (rand < float(color.get())):
                                    xval = int(x[0:2])
                                    yval = int(x[5:7])
                                    sensorId +=1
                                    s2 = c.create_oval(xval*4 + int(radius.get()) * 4,
                                                   yval*4 + int(radius.get()) * 4,
                                                   xval*4 - int(radius.get()) * 4,
                                                   yval*4 - int(radius.get()) * 4, stipple="gray12",
                                                   outline="Green",
                                                    tags=sensorId)
                                    s1 = c.create_oval(xval*4-2, yval*4-2, xval*4+2 , yval*4+2, stipple="gray12" ,
                                                                             outline="Green",
                                                                                fill="light green",tags=sensorId)
                                    s3 = c.create_text(xval*4 + 8,
                                                   yval*4 + 8,
                                                   font="Times 10 italic bold", text=sensorId)
                                    s = str(id) + " " + str(round(int(xval))) + ".00 " + str(round(int(yval))) + ".00 "
                                    calcSensorID.append(s)
                                    print(calcSensorID)
                                    id += 1;
                    else :
                                    xval = int(x[0:2])
                                    yval = int(x[5:7])
                                    sensorId += 1
                                    s2 = c.create_oval(xval * 4 + int(radius.get()) * 4,
                                           yval * 4 + int(radius.get()) * 4,
                                           xval * 4 - int(radius.get()) * 4,
                                           yval * 4 - int(radius.get()) * 4, stipple="gray12",
                                           outline="Red",
                                           tags=sensorId)
                                    s1 = c.create_oval(xval * 4 - 2, yval * 4 - 2, xval * 4 + 2, yval * 4 + 2, stipple="gray12",
                                           outline="Green",
                                           fill="light green", tags=sensorId)
                                    s3 = c.create_text(xval * 4 + 8,
                                           yval * 4 + 8,
                                           font="Times 10 italic bold", text=sensorId)
                                    s = str(id) + " " + str(round(int(xval))) + ".00 " + str(round(int(yval))) + ".00 "
                                    calcSensorID.append(s)
                                    print(calcSensorID)
                                    id += 1;
                RadioVariable = variableRadio.get()
                longb = 5
                i = 0
                if(RadioVariable=="36"):
                                for x in range(6):
                                                c.create_rectangle(0 + i, 0, 0 + i + longb, 5, fill="black")
                                                c.create_rectangle(0 + i, 66, 0 + i + longb, 71, fill="black")
                                                c.create_rectangle(0 + i, 133, 0 + i + longb, 138, fill="black")
                                                c.create_rectangle(0 + i, 199, 0 + i + longb, 204, fill="black")
                                                c.create_rectangle(0 + i, 265, 0 + i + longb, 270, fill="black")
                                                c.create_rectangle(0 + i, 331, 0 + i + longb, 336, fill="black")
                                                i = i + 66;
                                # battery = c.create_rectangle(0, 0, 10, 10, fill='red')
                elif (RadioVariable == "144"):
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
                                                i = i + 33
                elif (RadioVariable == "411"):
                                        for x in range(20):
                                                c.create_rectangle(0 + i, 0, 0 + i + longb, 2, fill="black")
                                                c.create_rectangle(0 + i, 20, 0 + i + longb, 22, fill="black")
                                                c.create_rectangle(0 + i, 40, 0 + i + longb, 42, fill="black")
                                                c.create_rectangle(0 + i, 60, 0 + i + longb, 62, fill="black")
                                                c.create_rectangle(0 + i, 80, 0 + i + longb, 82, fill="black")
                                                c.create_rectangle(0 + i, 100, 0 + i + longb, 102, fill="black")
                                                c.create_rectangle(0 + i, 120, 0 + i + longb, 122, fill="black")
                                                c.create_rectangle(0 + i, 140, 0 + i + longb, 142, fill="black")
                                                c.create_rectangle(0 + i, 160, 0 + i + longb, 162, fill="black")
                                                c.create_rectangle(0 + i, 180, 0 + i + longb, 182, fill="black")
                                                c.create_rectangle(0 + i, 200, 0 + i + longb, 202, fill="black")
                                                c.create_rectangle(0 + i, 220, 0 + i + longb, 222, fill="black")
                                                c.create_rectangle(0 + i, 240, 0 + i + longb, 242, fill="black")
                                                c.create_rectangle(0 + i, 260, 0 + i + longb, 262, fill="black")
                                                c.create_rectangle(0 + i, 280, 0 + i + longb, 282, fill="black")
                                                c.create_rectangle(0 + i, 300, 0 + i + longb, 302, fill="black")
                                                c.create_rectangle(0 + i, 320, 0 + i + longb, 322, fill="black")
                                                c.create_rectangle(0 + i, 340, 0 + i + longb, 342, fill="black")
                                                c.create_rectangle(0 + i, 360, 0 + i + longb, 362, fill="black")
                                                c.create_rectangle(0 + i, 380, 0 + i + longb, 382, fill="black")
                                                c.create_rectangle(0 + i, 400, 0 + i + longb, 402, fill="black")
                                                i = i + 20

                listSenss.extend(listSens)

        def Exit():
                        python = sys.executable
                        os.execl(python, python, *sys.argv)

        def SaveFile():
                        with open("MySensors .txt", 'w') as file:
                                for row in listSenss:
                                        s = "".join(map(str, row))
                                        file.write(s + '\n')
        def SaveFileSens():
                        with open("sensorId.txt", 'w') as file:
                                for row in calcSensorID:
                                        s = "".join(map(str, row))
                                        file.write(s + '\n')

        def donothing():  # HELPER
                        x = 0

                ####################################CZYTAJ PLik ####################################################################################
        def OpenSernsorId(): #SENSOR ID FILE
                        text_file = filedialog.askopenfilename(initialdir="C:/", title="Open TextFile",
                                                               filetypes=(("Text Files", "*.txt"),))
                        text_file = open(text_file, 'r')
                        for x in text_file:
                                ListofNumbers.append(x)
                        ListofNumbers.pop(0)
                        for x in ListofNumbers:
                                print(x)
                        for x in ListofNumbers:
                                xx=x[2:4]
                                yy=x[8:10]
                                id=x[0]
                                red=random.randint(0,2)
                                if red==1:
                                        colo="red"
                                else:
                                        colo="green"
                                print(xx+" "+yy)
                                c.create_oval(int(xx)*4, int(yy)*4,int(xx)*4+2,int(yy)*4+2,stipple="gray50",
                                                   fill="green", width=1,tags=id)
                                c.create_oval(int(xx)*4+25,
                                                   int(yy)*4+25,
                                                   int(xx)*4-25,
                                                   int(yy)*4-25,
                                                   fill=colo)
                                c.create_text(int(xx)*4 +8,
                                              int(yy)*4 +8,
                                              font="Times 10 italic bold", text=id)
        def OpenMYSensor():  # SENSOR ID FILE
                                        text_file = filedialog.askopenfilename(initialdir="C:/", title="Open TextFile",
                                                                               filetypes=(("Text Files", "*.txt"),))
                                        text_file = open(text_file, 'r')
                                        #DELETE FIRST PARAMETER
                                        for x in text_file:
                                                ListofNumbers.append(x)
                                        ListofNumbers.pop(0)
                                        for x in ListofNumbers:
                                                print(x)

                                        for x in ListofNumbers:
                                                if (x[3]=='.'):
                                                        xx = [2]
                                                else:
                                                        xx = x[2:4]
                                                if (x[9]=='.'):
                                                        yy = x[8]
                                                else:
                                                        yy=x[8:10]
                                                id=x[0]
                                                red = random.randint(0, 2)
                                                if red == 1:
                                                        colo = "red"
                                                else:
                                                        colo = "light green"
                                                print(xx + " " + yy)
                                                c.create_oval(int(xx) * 4, int(yy) * 4, int(xx) * 4 + 2,
                                                              int(yy) * 4 + 2, stipple="gray50",
                                                              fill="green", width=1, tags=id)
                                                c.create_oval(int(xx) * 4 + 25,
                                                              int(yy) * 4 + 25,
                                                              int(xx) * 4 - 25,
                                                              int(yy) * 4 - 25,
                                                              fill=colo)
                                                c.create_text(int(xx) * 4 + 8,
                                                              int(yy) * 4 + 8,
                                                              font="Times 10 italic bold", text=id)
        def OpenSensorWSN():
                        id=1
                        listSens= []
                        text_file = filedialog.askopenfilename(initialdir="C:/", title="Open TextFile",
                                                               filetypes=(("Text Files", "*.txt"),))
                        text_file = open(text_file, 'r')
                        # DELETE FIRST PARAMETER
                        for x in text_file:
                                ListofNumbers.append(x)
                        ListofNumbers.pop(0)
                        for x in ListofNumbers:
                                print(x)

                        for x in ListofNumbers:
                                xx=x[0:2]
                                yy=x[5:7]

                                red = random.randint(0, 2)
                                if red == 1:
                                        colo = "red"
                                else:
                                        colo = "green"
                                print(xx + " " + yy)
                                c.create_oval(int(xx) * 4, int(yy) * 4, int(xx) * 4 + 2, int(yy) * 4 + 2,
                                              stipple="gray50",
                                              fill="green", width=1, tags=id)
                                c.create_oval(int(xx) * 4 + int(radius.get()) * 4,
                                              int(yy) * 4 + int(radius.get()) * 4,
                                              int(xx) * 4 - int(radius.get()) * 4,
                                              int(yy) * 4 - int(radius.get()) * 4,
                                              outline=colo)
                                c.create_text(int(xx) * 4 + 8,
                                              int(yy) * 4 + 8,
                                              font="Times 10 italic bold", text=id)
                                s = str(id) + " " + str(round(int(xx))) + ".00 " + str(round(int(yy))) + ".00 "
                                calcSensorID.append(s)
                                print(calcSensorID)
                                id+=1;

        def OpenMYSensorNeighbour(): #find WSN grapph
                        text_file = filedialog.askopenfilename(initialdir="C:/", title="Open TextFile",
                                                               filetypes=(("Text Files", "*.txt"),))
                        text_file = open(text_file, 'r')
                        for x in text_file:
                                ListofNumbers.append(x)
                        ListofNumbers.pop(0)
                        for x in ListofNumbers:
                                print(x)
                        # LIST NEIGTBOUR
                        ListSensorneigh.append("#parameters of run: ")
                        ListSensorneigh.append("#Number of Sensors " + str(amountReadWSN))
                        ListSensorneigh.append("#Sensor Range: " + str(radius.get()))
                        ListSensorneigh.append("#POI: "+str(variableRadio.get()))
                        ListSensorneigh.append("#Sensor for file: " + str(text_file.name))
                        ListSensorneigh.append("#id num_of_neighb neigb-ID")
                        id = 1
                        text_filed = open("FILES/WSN-5d.txt")
                        for x in ListofNumbers:
                                xx = x[0:2]
                                yy = x[5:7]
                                c.create_oval(int(xx) * 4-2, int(yy) * 4-2, int(xx) * 4 + 2,
                                              int(yy) * 4 + 2, stipple="gray50",
                                              outline="green",fill="green", width=1)
                                c.create_oval(int(xx) * 4 - (int(radius.get())*4),
                                              int(yy) * 4 - (int(radius.get())*4),
                                              int(xx) * 4 + (int(radius.get())*4),
                                              int(yy) * 4 + (int(radius.get())*4),
                                              outline="Green", tags=id)
                                c.create_text(int(xx) * 4 + 15, int(yy) * 4 + 15,
                                              font="Times 10 italic bold", text=id)
                                id += 1;

                        def circle(x1, y1, x2, y2, r1, r2):
                            distSq = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
                            radSumSq = (r1 + r2) * (r1 + r2)
                            if (distSq == radSumSq):
                                return 1
                            elif (distSq > radSumSq):
                                return -1
                            else:
                                return 0

                        ys = ""
                        counter = 1
                        for x in ListofNumbers:
                            id=1
                            helper = 0
                            for y in ListofNumbers:
                                    ListofNeighbour.append(str(id) + str(circle(int(x[0:2]),int(y[0:2]), int(x[5:7]),int(y[5:7]),int(radius.get()),int(radius.get()))))
                                    xs=str(id) + str(circle(int(x[0:2]),int(y[0:2]), int(x[5:7]),int(y[5:7]),int(radius.get()),int(radius.get())))
                                    beng='-'
                                    if(beng in xs or  str(counter) == xs[0:1]):
                                        donothing()
                                    else:
                                        if(len(xs)<3):
                                            ys+=xs[0]
                                            helper=helper+1
                                        else:
                                            ys+=xs[0:2]
                                            helper = helper + 1
                                    id = id + 1
                            ListSensorneigh.append(str(counter) + "    "+str(helper) + "     " +ys)
                            ys=""
                            ListofNeighbour.clear()
                            counter=counter+1
                        print(ListSensorneigh)
                        def SaveFileSenss():
                            with open("sensor-neighbours .txt", 'w') as file:
                                for row in ListSensorneigh:
                                    s = "".join(map(str, row))
                                    file.write(s + '\n')
                        SaveFileSenss()
                ###########################################################################################


        menubar = tk.Menu(main_window)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=donothing)
        filemenu.add_command(label="Open FILE: [SensorId]", command=OpenSernsorId)
        filemenu.add_command(label="Open FILE: [MySensorId]", command=OpenMYSensor)
        filemenu.add_command(label="Open FILE: [sensor-states]", command=OpenMYSensorStates)
        filemenu.add_command(label="Open FILE: [WSN]", command=OpenSensorWSN)
        filemenu.add_command(label="Open FILE: [OpenMYSensorNeighbour]", command=OpenMYSensorNeighbour)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=main_window.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        myButton = tk.Button(main_window, text="SHOW WSN", command=Init)
        myButton.pack()
        ExitButton = tk.Button(main_window,text="EXIT",command=Exit)
        ExitButton.pack(side="right")
        SaveButton=tk.Button(main_window,text="cal sensor ID",command=SaveFileSens)
        SaveButton.pack(side="left")
        SaveButton = tk.Button(main_window, text="find WSN graph", command=OpenMYSensorNeighbour)
        SaveButton.pack(side="left")
        main_window.config(menu=menubar)
#########################################################################################################################

        #INSTANCE
        main_window.mainloop()
