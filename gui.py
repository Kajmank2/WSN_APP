import random
import csv
from functools import reduce
from tkinter import filedialog
import tkinter as tk
import os
import sys
s="#id x y"
listSenss = []
ListXySensCov=[]
ListSensorneigh=[]
ListCover=[]
ListPOI=[]
ALLPOICOV=[]
Poir=4
calcSensorID=[]
calcSensorID.append(s)
SquareArenas=40000
Pi=3.14
amountReadWSN=0
def InitGui():
        main_window =tk.Tk()
        ListofNumbers=[]
        ListofNumbersCalcSingleq=[]
        converted_listCalcSingleq = []
        ListofNumbersCalcSingleqState=[]
        ListPOI = []
        IdPOICOV=[]
        SensorHelper=[]
        SensorHelperPoiID=[]
        ListofNeighbour=[]

        tk.Label(text="X 0-100").pack(side="bottom")
        tk.Label(text="Y 0-100").pack(side="left")
        c = tk.Canvas(main_window, width=400, height=400, bg="white")
        c.pack(side="left")
        #POI 411
        #FIRST POI
        def OpenMYSensorStates(): #SENSOR ID FILE
                        text_file = filedialog.askopenfilename(initialdir="C:/", title="Open TextFile",
                                                               filetypes=(("Text Files", "*.txt"),))
                        text_file = open(text_file, 'r')
                        listSenss.clear() #CLEAR LIST
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
        longb=2
        i=0
        for x in range(6):
            c.create_oval(0 + i, 0, 0 + i + longb, 4, fill="black")
            s = "" + str(0 + i / 4) + " " + str(0 / 4)
            ListPOI.append(s)
            c.create_oval(0 + i, 66, 0 + i + longb, 70, fill="black")
            s = "" + str(0 + i / 4) + " " + str(68 / 4)
            ListPOI.append(s)
            c.create_oval(0 + i, 134, 0 + i + longb, 138, fill="black")
            s = "" + str(0 + i / 4) + " " + str(136 / 4)
            ListPOI.append(s)
            c.create_oval(0 + i, 200, 0 + i + longb, 204, fill="black")
            s = "" + str(0 + i / 4) + " " + str(202 / 4)
            ListPOI.append(s)
            c.create_oval(0 + i, 264, 0 + i + longb, 270, fill="black")
            s = "" + str(0 + i / 4) + " " + str(268 / 4)
            ListPOI.append(s)
            c.create_oval(0 + i, 332, 0 + i + longb, 336, fill="black")
            s = "" + str(0 + i / 4) + " " + str(334 / 4)
            ListPOI.append(s)
            i = i + 66;
        # DLA POI 411 -------
        '''
        for x in range(21):
                c.create_oval(0 + i, 0, 0 + i + longb, 2, fill="black")
                s=""+str(0+i/4) + " " + str(0/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 20, 0 + i + longb, 22, fill="black")
                s = "" + str(0 + i/4) + " " + str(20/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 40, 0 + i + longb, 42, fill="black")
                s = "" + str(0 + i/4) + " " + str(40/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 60, 0 + i + longb, 62, fill="black")
                s = "" + str(0 + i/4) + " " + str(60/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 80, 0 + i + longb, 82, fill="black")
                s = "" + str(0 + i/4) + " " + str(80/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 100, 0 + i + longb, 102, fill="black")
                s = "" + str(0 + i/4) + " " + str(100/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 120, 0 + i + longb, 122, fill="black")
                s = "" + str(0 + i/4) + " " + str(120/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 140, 0 + i + longb, 142, fill="black")
                s = "" + str(0 + i/4) + " " + str(140/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 160, 0 + i + longb, 162, fill="black")
                s = "" + str(0 + i/4) + " " + str(160/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 180, 0 + i + longb, 182, fill="black")
                s = "" + str(0 + i/4) + " " + str(180/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 200, 0 + i + longb, 202, fill="black")
                s = "" + str(0 + i/4) + " " + str(200/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 220, 0 + i + longb, 222, fill="black")
                s = "" + str(0 + i/4) + " " + str(220/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 240, 0 + i + longb, 242, fill="black")
                s = "" + str(0 + i/4) + " " + str(240/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 260, 0 + i + longb, 262, fill="black")
                s = "" + str(0 + i/4) + " " + str(260/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 280, 0 + i + longb, 282, fill="black")
                s = "" + str(0 + i/4) + " " + str(280/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 300, 0 + i + longb, 302, fill="black")
                s = "" + str(0 + i/4) + " " + str(300/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 320, 0 + i + longb, 322, fill="black")
                s = "" + str(0 + i/4) + " " + str(320/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 340, 0 + i + longb, 342, fill="black")
                s = "" + str(0 + i/4) + " " + str(340/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 360, 0 + i + longb, 362, fill="black")
                s = "" + str(0 + i/4) + " " + str(360/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 380, 0 + i + longb, 382, fill="black")
                s = "" + str(0 + i/4) + " " + str(380/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 400, 0 + i + longb, 402, fill="black")
                s = "" + str(0 + i/4) + " " + str(400/4)
                ListPOI.append(s)
                i = i + 20
                #X and Y
                print(ListPOI)
                # ENTRY
            '''
        def SaveFile():
                        with open("MYPOI .txt", 'w') as file:
                                for row in ListPOI:
                                        s = "".join(map(str, row))
                                        file.write(s + '\n')
        SaveFile()
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
        def CalcSingleq():  # calc single q
            r=35
            SensorStates=[]
            coverage = 0.0
            ListPOI.clear()
            with open('POI36.csv') as file:  # CHANGE TO PO 4412
                reader=csv.reader(file)
                for row in reader:
                    print(row)
                    ListPOI.append(row)
            '''
            ms.showinfo(title=None, message="Read Sensor States")
            text_fileq = filedialog.askopenfilename(initialdir="C:/", title="Open TextFile",
                                                    filetypes=(("Text Files", "*.txt"),))
            state=[]
            text_fileq = open(text_fileq, 'r')
            '''
            state = []
            text_fileq = open("FILES/sensor-states-10.txt") #do usuniecia potem STEJTY
            for x in text_fileq:
                ListofNumbersCalcSingleqState.append(x)
                state.append(x[12])
            ListofNumbersCalcSingleqState.pop(0)
            state.pop(0)
            print(ListofNumbersCalcSingleqState)
            print(state)
            '''
            ms.showinfo(title=None, message="READ WSN FILE")
            text_file = filedialog.askopenfilename(initialdir="C:/", title="Open TextFile",
                                                   filetypes=(("Text Files", "*.txt"),))
            text_file = open(text_file, 'r')
            '''
            text_file = open("FILES/WSN-5d.txt")
            for x in text_file:
                ListofNumbersCalcSingleq.append(x)
                print(ListofNumbersCalcSingleq)
            ListofNumbersCalcSingleq.pop(0)
            for x in ListofNumbersCalcSingleq:
                converted_listCalcSingleq.append(x.strip())
            for i in range(len(converted_listCalcSingleq)):
                converted_listCalcSingleq[i]+= state[i]
            print(converted_listCalcSingleq)

            # LIST NEIGTBOUR
            ListSensorneigh.append("#parameters of run: ")
            ListSensorneigh.append("#Number of Sensors " + "5")
            ListSensorneigh.append("#Sensor Range: " + str(radius.get()))
            ListSensorneigh.append("#POI: " + str(variableRadio.get()))
            ListSensorneigh.append("#Sensor for file: " + str(text_file.name))
            ListSensorneigh.append("Sensor for file: :WSN-5d-test0.txt")
            ListSensorneigh.append("#q    s    1 2 3 4 5   q1   q2   q3   q4   q5")
            id = 1
            for x in converted_listCalcSingleq:
                xx = x[0:2]
                yy = x[5:7]
                state=x[9]
                print(state)
                if state == '0':
                    colo = "red"
                else:
                    colo = "green"
                c.create_oval(int(xx) * 4 - 2, int(yy) * 4 - 2, int(xx) * 4 + 2,
                              int(yy) * 4 + 2, stipple="gray50",
                              outline="green", fill="green", width=1)
                c.create_oval(int(xx) * 4 - (int(radius.get()) * 4),
                              int(yy) * 4 - (int(radius.get()) * 4),
                              int(xx) * 4 + (int(radius.get()) * 4),
                              int(yy) * 4 + (int(radius.get()) * 4),
                              outline=colo, tags=id)
                c.create_text(int(xx) * 4 + 15, int(yy) * 4 + 15,
                              font="Times 10 italic bold", text=id)
                SensorStates.append(state)
                id += 1;

            print(ListSensorneigh)
            als = "" # Value helper
            def circle(x1, y1, x2, y2, r1, r2):
                distSq = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
                radSumSq = (r1 + r2) * (r1 + r2)
                if (distSq == radSumSq):
                    return 1
                elif (distSq > radSumSq):
                    return -1
                else:
                    return 0

            #POI TO 1d ARRAY
            flaten_list=reduce(lambda z, y :z + y,ListPOI)

            ys=""
            counter = 1
            ids = 1
            # OBLICZANIE POKRYCIE KAŻDEGO SENSORA
            for x in converted_listCalcSingleq:
                helper = 0
                for y in flaten_list:
                    if(y[0]=='0'or y[0:2]=='5;'): #SOLUCJA ZAPISAC CSV JAKO CIĄG STRINGÓW NIE OSOBNĄ LISTE
                        SensorHelper.append(str(circle(int(x[0:2]),int(x[5:7]), int(y[0]),  int(y[2:]), int(radius.get()),Poir)))
                        ys=str(circle(int(x[0:2]),int(x[5:7]), int(y[0]),  int(y[2:]), int(radius.get()),Poir))
                        if (ys[0] == '0'):
                            donothing()
                        else:
                            helper += 1 #VALUE WHEN SENSOR STATE IS 1
                    elif(y[0:3]=='100'):
                        SensorHelper.append(
                            str(circle(int(x[0:2]), int(x[5:7]) ,int(y[0:3]),  int(y[4:]), int(radius.get()), Poir)))
                        ys=str(circle(int(x[0:2]), int(x[5:7]) ,int(y[0:3]),  int(y[4:]), int(radius.get()), Poir))
                        if (ys[0] == '0'):
                            donothing()
                        else:
                            helper += 1
                    else:
                        SensorHelper.append(
                            str(circle(int(x[0:2]),  int(x[5:7]), int(y[0:2]), int(y[3:]), int(radius.get()), Poir)))
                        ys=str(circle(int(x[0:2]),  int(x[5:7]), int(y[0:2]), int(y[3:]), int(radius.get()), Poir))
                        if(ys[0]=='0'):
                            donothing()
                        else:
                            helper+=1

                coverage=36-helper # ZMINA Z 411
                IdPOICOV.append(str(coverage)) # ID + AMOUNT OF
                pom=0
                for x in SensorHelper:
                    ALLPOICOV.append(x)
                    SensorHelperPoiID.append(x+ " - " + str(pom))
                    pom=pom+1
               # ALLPOICOV.extend(SensorHelper)
                ids += 1
                SensorHelper.clear()
            ########################################## END POI AMOUNT####################
            chunkser = [ALLPOICOV[x:x + 36] for x in range(0, len(ALLPOICOV), 36)] # ZMIANA Z 411
            chunkserPoi=[SensorHelperPoiID[x:x + 36] for x in range(0, len(SensorHelperPoiID), 36)] # POI in EVERY SENSEOR
            print(chunkser)
            print("POI COV")
            print(ALLPOICOV)
            print("COVEREGE SENSOR BY POI")
            print(IdPOICOV)
            idstates=0
            arubaCloud=[]
            counterchuk=0
            amount=0
            abc=""
            for x in SensorStates:
                if(x=='0'):
                    donothing()
                else:
                    trucrypt = chunkser[counterchuk]
                    for y in chunkser:
                        printerek=0
                        amount = 0
                        for z in y:
                                if(trucrypt[printerek]==z):
                                    if(z=='0' ): #and trucrypt != y
                                        amount=amount+1
                                        arubaCloud.append(str(printerek)) # USUNIECIE PRINTERKA
                                else:
                                    donothing()
                                printerek=printerek+1
                        abc += str(idstates)+ "-" + str(amount) + "\n" #AMOUNT + STATES ON
                counterchuk=counterchuk+1
                idstates=idstates+1
            finalStates=dict.fromkeys(arubaCloud) #DELETE DUPLICATE
            #COVERAGE Q
            coverageQ=len(finalStates)/36
            # COVERAGE EVERY Q
            qoverageString=0
            Lista = []
            strPoi=""
            for x in chunkserPoi:
                for y in x:
                    if(y[0:2]=='-1'):
                        donothing()
                    else:
                        strPoi+=y+"."
                Lista.append(strPoi) # WSZYSTKIe POI ID z Pokryciem
                strPoi=""

            def calsum(l):
                # returning sum of list using List comprehension
                return sum([int(i) for i in l if type(i) == int or i.isdigit()])
            # DLA 36 trening
            ListwihCov=[]
            asa="0"
            ListwihCovPercent=[]
            idCoverage=1
            for x in Lista:
                    abc=x.split('.')
                    helperCov=0
                    for z in abc:
                        for y in finalStates:
                            if(z[4:]==y):
                                helperCov=helperCov+1
                    asa= str(helperCov)    #str(helperCov - calsum(ListwihCov))
                    abc.clear()
                    idCoverage+=1
                    #Calculate % POV
                    ListwihCov.append(asa)
            # LIST CALCULATION
            z=[int(x) for x in ListwihCov]
            x=([int(x) for x in IdPOICOV])
            products = [a / b for a, b in zip(z, x)]
            print(products)
            #CALC SENSOR ID TO TXT
            ListSensorneigh.append(str(coverageQ) + "  " + "10   " + ' '.join(SensorStates) + "   " + '  '.join(str(round(e,1)) for e in products))
            '''
            print("COVERAGE Q")
            print(ListSensorneigh)

            print("ASA")
            print(IdPOICOV)
            print(ListwihCov)
            print("STR POI")
            print(strPoi)
            print(Lista)
            print("ARUBA")
            print(arubaCloud)
            print("PO KONWERSJI")
            print(list(finalStates))
            '''


            def SaveFileSenss():
                with open("creates cov-10-WSN-5.txt"
                          "", 'w') as file:
                    for row in ListSensorneigh:
                        s = "".join(map(str, row))
                        file.write(s + '\n')

            SaveFileSenss()
                ###########################################################################################

        def CalcALLq():  # calc single q
            SensorStates=[]
            ListPOI.clear()
            with open('POI36.csv') as file:  # CHANGE TO PO 4412
                reader=csv.reader(file)
                for row in reader:
                    print(row)
                    ListPOI.append(row)
            '''
            ms.showinfo(title=None, message="Read Sensor States")
            text_fileq = filedialog.askopenfilename(initialdir="C:/", title="Open TextFile",
                                                    filetypes=(("Text Files", "*.txt"),))
            state=[]
            text_fileq = open(text_fileq, 'r')
            '''
            state = []
            text_fileq = open("FILES/sensor-states-10.txt") #do usuniecia potem STEJTY
            for x in text_fileq:
                ListofNumbersCalcSingleqState.append(x)
                state.append(x[12])
            ListofNumbersCalcSingleqState.pop(0)
            state.pop(0)
            print(ListofNumbersCalcSingleqState)
            print(state)
            '''
            ms.showinfo(title=None, message="READ WSN FILE")
            text_file = filedialog.askopenfilename(initialdir="C:/", title="Open TextFile",
                                                   filetypes=(("Text Files", "*.txt"),))
            text_file = open(text_file, 'r')
            '''
            text_file = open("FILES/WSN-5d.txt")
            for x in text_file:
                ListofNumbersCalcSingleq.append(x)
                print(ListofNumbersCalcSingleq)
            ListofNumbersCalcSingleq.pop(0)
            for x in ListofNumbersCalcSingleq:
                converted_listCalcSingleq.append(x.strip())
            for i in range(len(converted_listCalcSingleq)):
                converted_listCalcSingleq[i]+= state[i]
            print(converted_listCalcSingleq)
            ListSensorneigh.clear()
            # LIST NEIGTBOUR
            ListSensorneigh.append("#parameters of run: ")
            ListSensorneigh.append("#Number of Sensors " + "5")
            ListSensorneigh.append("#Sensor Range: " + str(radius.get()))
            ListSensorneigh.append("#POI: " + str(variableRadio.get()))
            ListSensorneigh.append("#Sensor for file: " + str(text_file.name))
            ListSensorneigh.append("Sensor states for file: not appiled")
            ListSensorneigh.append("#id q    s    1 2 3 4 5   q1   q2   q3   q4   q5")
            id = 1
            '''
            for x in converted_listCalcSingleq:
                xx = x[0:2]
                yy = x[5:7]
                state=x[9]
                print(state)
                if state == '0':
                    colo = "red"
                else:
                    colo = "green"
                c.create_oval(int(xx) * 4 - 2, int(yy) * 4 - 2, int(xx) * 4 + 2,
                              int(yy) * 4 + 2, stipple="gray50",
                              outline="green", fill="green", width=1)
                c.create_oval(int(xx) * 4 - (int(radius.get()) * 4),
                              int(yy) * 4 - (int(radius.get()) * 4),
                              int(xx) * 4 + (int(radius.get()) * 4),
                              int(yy) * 4 + (int(radius.get()) * 4),
                              outline=colo, tags=id)
                c.create_text(int(xx) * 4 + 15, int(yy) * 4 + 15,
                              font="Times 10 italic bold", text=id)
                SensorStates.append(state)
                id += 1;
                '''
            print(ListSensorneigh)
            def circle(x1, y1, x2, y2, r1, r2):
                distSq = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
                radSumSq = (r1 + r2) * (r1 + r2)
                if (distSq == radSumSq):
                    return 1
                elif (distSq > radSumSq):
                    return -1
                else:
                    return 0

            #POI TO 1d ARRAY
            flaten_list=reduce(lambda z, y :z + y,ListPOI)
            ids = 1
            # OBLICZANIE POKRYCIE KAŻDEGO SENSORA
            for x in converted_listCalcSingleq:
                helper = 0
                for y in flaten_list:
                    if(y[0]=='0'or y[0:2]=='5;'): #SOLUCJA ZAPISAC CSV JAKO CIĄG STRINGÓW NIE OSOBNĄ LISTE
                        SensorHelper.append(str(circle(int(x[0:2]),int(x[5:7]), int(y[0]),  int(y[2:]), int(radius.get()),Poir)))
                        ys=str(circle(int(x[0:2]),int(x[5:7]), int(y[0]),  int(y[2:]), int(radius.get()),Poir))
                        if (ys[0] == '0'):
                            donothing()
                        else:
                            helper += 1 #VALUE WHEN SENSOR STATE IS 1
                    elif(y[0:3]=='100'):
                        SensorHelper.append(
                            str(circle(int(x[0:2]), int(x[5:7]) ,int(y[0:3]),  int(y[4:]), int(radius.get()), Poir)))
                        ys=str(circle(int(x[0:2]), int(x[5:7]) ,int(y[0:3]),  int(y[4:]), int(radius.get()), Poir))
                        if (ys[0] == '0'):
                            donothing()
                        else:
                            helper += 1
                    else:
                        SensorHelper.append(
                            str(circle(int(x[0:2]),  int(x[5:7]), int(y[0:2]), int(y[3:]), int(radius.get()), Poir)))
                        ys=str(circle(int(x[0:2]),  int(x[5:7]), int(y[0:2]), int(y[3:]), int(radius.get()), Poir))
                        if(ys[0]=='0'):
                            donothing()
                        else:
                            helper+=1

                coverage=36-helper # ZMINA Z 411
                IdPOICOV.append(str(coverage)) # ID + AMOUNT OF
                pom=0
                for x in SensorHelper:
                    ALLPOICOV.append(x)
                    SensorHelperPoiID.append(x+ " - " + str(pom))
                    pom=pom+1
               # ALLPOICOV.extend(SensorHelper)
                ids += 1
                SensorHelper.clear()
            ########################################## END POI AMOUNT####################
            chunkser = [ALLPOICOV[x:x + 36] for x in range(0, len(ALLPOICOV), 36)] # ZMIANA Z 411
            chunkserPoi=[SensorHelperPoiID[x:x + 36] for x in range(0, len(SensorHelperPoiID), 36)] # POI in EVERY SENSEOR
            print(chunkser)
            print("POI COV")
            print(ALLPOICOV)
            print("COVEREGE SENSOR BY POI")
            print(IdPOICOV)
            idstates=0
            arubaCloud=[]
            counterchuk=0
            amount=0
            abc=""
            #FORMAT
            BinaryList=[]
            for x in range (0,32):
                Binary='{:05b}'.format(x)
                BinaryList.append(Binary)
            print(BinaryList)
            for x in BinaryList:
             for z in x:
                if(z=='0'):
                    donothing()
                else:
                    trucrypt = chunkser[counterchuk]
                    for y in chunkser:
                        printerek=0
                        amount = 0
                        for z in y:
                                if(trucrypt[printerek]==z):
                                    if(z=='0' ): #and trucrypt != y
                                        amount=amount+1
                                        arubaCloud.append(str(printerek)) # USUNIECIE PRINTERKA
                                else:
                                    donothing()
                                printerek=printerek+1
                        abc += str(idstates)+ "-" + str(amount) + "\n" #AMOUNT + STATES ON
                counterchuk=counterchuk+1
                idstates=idstates+1
            finalStates=dict.fromkeys(arubaCloud) #DELETE DUPLICATE
            #COVERAGE Q
            coverageQ=len(finalStates)/36
            # COVERAGE EVERY Q
            qoverageString=0
            Lista = []
            strPoi=""
            for x in chunkserPoi:
                for y in x:
                    if(y[0:2]=='-1'):
                        donothing()
                    else:
                        strPoi+=y+"."
                Lista.append(strPoi) # WSZYSTKIe POI ID z Pokryciem
                strPoi=""

            def calsum(l):
                # returning sum of list using List comprehension
                return sum([int(i) for i in l if type(i) == int or i.isdigit()])
            # DLA 36 trening
            ListwihCov=[]
            asa="0"
            ListwihCovPercent=[]
            idCoverage=1
            for x in Lista:
                    abc=x.split('.')
                    helperCov=0
                    for z in abc:
                        for y in finalStates:
                            if(z[4:]==y):
                                helperCov=helperCov+1
                    asa= str(helperCov)    #str(helperCov - calsum(ListwihCov))
                    abc.clear()
                    idCoverage+=1
                    #Calculate % POV
                    ListwihCov.append(asa)
            # LIST CALCULATION
            z=[int(x) for x in ListwihCov]
            x=([int(x) for x in IdPOICOV])
            products = [a / b for a, b in zip(z, x)]
            print(products)
            #CALC SENSOR ID TO TXT
            idAllq=0
            ListSensorneigh.append(str(idAllq)+ " "+str(coverageQ) + "  " + "10   " + ' '.join(SensorStates) + "   " + '  '.join(str(round(e,1)) for e in products))
            ListSensorneigh.append("0   0.00  0   0 0 0 0 0   0.00 0.00 0.00 0.00 0.00 ")
            def SaveFileSenss():
                with open("creates all-WSN-5.txt"
                          "", 'w') as file:
                    for row in ListSensorneigh:
                        s = "".join(map(str, row))
                        file.write(s + '\n')

            SaveFileSenss()

            print("COVERAGE Q")
            print(ListSensorneigh)

            print("ASA")
            print(IdPOICOV)
            print(ListwihCov)
            print("STR POI")
            print(strPoi)
            print(Lista)
            print("ARUBA")
            print(arubaCloud)
            print("PO KONWERSJI")
            print(list(finalStates))



        myButton = tk.Button(main_window, text="SHOW WSN", command=Init)
        myButton.pack()
        ExitButton = tk.Button(main_window,text="EXIT",command=Exit)
        ExitButton.pack(side="right")
        SaveButton=tk.Button(main_window,text="cal sensor ID",command=SaveFileSens)
        SaveButton.pack(side="left")
        SaveButton = tk.Button(main_window, text="find WSN graph", command=OpenMYSensorNeighbour)
        SaveButton.pack(side="left")
        SaveButton = tk.Button(main_window, text="calc single q", command=CalcSingleq)
        SaveButton.pack(side="left")
        SaveButton = tk.Button(main_window, text="calc all q", command=CalcALLq)
        SaveButton.pack(side="left")

#########################################################################################################################

        #INSTANCE
        main_window.mainloop()
