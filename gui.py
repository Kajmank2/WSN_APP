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
ListCover=[]
calcSensorID=[]
listSenss.append(s)
SquareArenas=160000/4


def InitGui():
        main_window =tk.Tk()
        scrollbar = tk.Scrollbar(main_window,orient = 'vertical')
        scrollbar.pack(side='right', fill='y')
        #PADY , PADX - PADDINGI
        ListofNumbers=[]
        ListofNumbersd = []
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
                c.create_line(0, 0, 0, 400, fill="black", width=3)

                #X and Y
                # ENTRY
                count = tk.StringVar()
                radius = tk.StringVar()
                color = tk.StringVar()
                battery = tk.StringVar()
                count.set("5")
                radius.set("20")
                color.set("0.5")
                battery.set("20")


                tk.Label(text="COUNT").pack()
                countSens = tk.Entry(main_window,textvariable =count, width=10, borderwidth=5, ).pack()
                tk.Label(text="RADIUS").pack()
                radiusSens = tk.Entry(main_window,textvariable =radius ,width=10, borderwidth=5).pack()
                tk.Label(text="Battery Capacity").pack()
                batteryCapacity = tk.Entry(main_window, textvariable=battery, width=10, borderwidth=5).pack()
                tk.Label(text="% Sensor Activity VALUE: 0-1").pack()
                propabilityEntry = tk.Entry(main_window, textvariable=color, width=10, borderwidth=5).pack()


                #VARIABLES FOR STATMENT
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
                                i = i + 20;

                def Init():
                        sensorId=0
                        listSens= []
                        SquareArea = 160000.00/4
                        #List which save param for
                        countCIRCLE=int(count.get())
                        colores= float(count.get()) * float(color.get())
                        # COLOR FOR CIRCLE
                        for colorRed in range (1,1+int(colores)):
                                sensorId +=1
                                xval = random.randint(10, 350)
                                yval = random.randint(10, 350)
                                s2 = c.create_oval(xval + int(radius.get()) * 4,
                                                   yval + int(radius.get()) * 4,
                                                   xval - int(radius.get()) * 4,
                                                   yval - int(radius.get()) * 4, stipple="gray12",
                                                   outline="Green",
                                                   fill="light green", tags=sensorId)
                                s1 = c.create_oval(xval-2, yval-2, xval+2 , yval+2, stipple="gray12" ,
                                                                             outline="Green",
                                                                                fill="light green",tags=sensorId)
                                s3 = c.create_text(xval + 8,
                                                   yval + 8,
                                                   font="Times 10 italic bold", text=sensorId)
                                s=str(sensorId)+" "+ str(round(xval/4))+ ".00 " + str(round(yval/4))+".00 "
                                tmp = float(radius.get()) * float(radius.get()) * 3.14
                                ListXySensCov.append("FIELD " + str(int(tmp)) + " X:"+str(int((xval + int(radius.get()) * 4 / 2)/4)) + " Y:"+ str(int((yval + int(radius.get()) * 4 / 2)/4)) + " R:"+ str(int(radius.get())))
                                listSens.append(s)
                                print(ListXySensCov)
                              #  print(ListXySensCov)
                              #  print(tmp)
                              #  SquareArea-=tmp
                              #  print(SquareArea)
                                # countSS += 1


                        # COLOR FOR CIRCLE
                        for colorGreen in range(1, 1 + countCIRCLE-int(colores)):
                                sensorId +=1
                                xval = random.randint(10, 300)
                                yval = random.randint(10, 300)
                                s2 = c.create_oval(xval + int(radius.get()) * 4,
                                                   yval + int(radius.get()) * 4,
                                                   xval - int(radius.get()) * 4,
                                                   yval - int(radius.get()) * 4, outline="red", tags=sensorId)
                                s1 = c.create_oval(xval - 2, yval - 2, xval + 2, yval + 2, stipple="gray12",
                                                   outline="Green",
                                                   fill="red", width=1)

                                s3 = c.create_text(xval + 8,
                                                   yval + 8,
                                                   font="Times 10 italic bold", text=sensorId)
                                #TXT FOR READ Value form file
                                s=str(sensorId)+" "+ str(round(xval/4))+ ".00 " + str(round(yval/4))+".00 "# + battery.get()
                                ListXySensCov.append("FIELD " + str(int(tmp)) + " X:"+str(int((xval + int(radius.get()) * 4 / 2)/4)) + " Y:"+ str(int((yval + int(radius.get()) * 4 / 2)/4)) + " R:"+ str(int(radius.get())))
                                x=str(int(xval/4)) + " " + str(int(yval/4)) + " " + str(int(radius.get()))

                                print(x)
                                listSens.append(s)
                                ListCover.append(x)
                                print(ListXySensCov)

                        #COVERAGE
                      #  Coverage=100 -SquareArea/SquareArenas * 100
                       # print(Coverage)
                      #  tk.Label(text="Coverage %").pack()
                      #  tk.Label(text=int(Coverage)).pack()
                      #  print(ListXySensCov)
                        # COVERAGE ==============================
                       # x=SquareArea-SquareTmp
                        #Coverage=SquareTmp/SquareArea*100
                       # Coverage=100-Coverage
                       # tk.Label(text="% covarage + ").pack()
                        #Write local to global
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
                        with open("SensorId .txt", 'w') as file:
                                for row in calcSensorID:
                                        s = "".join(map(str, row))
                                        file.write(s + '\n')

                def donothing():  # HELPER
                        x = 0

                ####################################CZYTAJ PLik ####################################################################################
                def OpenMYSensorStates(): #SENSOR ID FILE
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
                                yy=x[7:9]
                                id=x[0]
                                state=x[12]
                                if state=='0':
                                        colo="red"
                                else:
                                        colo="green"
                                print(xx+" "+yy)
                                print(state)
                                c.create_oval(int(xx) * 4, int(yy) * 4, int(xx) * 4 - 2, int(yy) * 4 + 2,
                                              stipple="gray50",
                                              fill="black", tags=id)
                                c.create_oval(int(xx) * 4 + 25,
                                              int(yy) * 4 + 25,
                                              int(xx) * 4 - 25,
                                              int(yy) * 4 - 25,
                                              stipple="gray50",
                                              outline=colo)
                                c.create_text(int(xx)*4 + 8,
                                              int(yy)*4 + 8,
                                              font="Times 10 italic bold", text=id)
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
                        id=0
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
                                s = str(id) + " " + str(round(xx / 4)) + ".00 " + str(round(yy / 4)) + ".00 "
                                calcSensorID.append(s)
                                print(calcSensorID)
                                id+=1;

                def OpenMYSensorNeighbour(): #SENSOR ID FILE
                        text_file = filedialog.askopenfilename(initialdir="C:/", title="Open TextFile",
                                                               filetypes=(("Text Files", "*.txt"),))
                        text_file = open(text_file, 'r')
                        for x in text_file:
                                ListofNumbers.append(x)
                        ListofNumbers.pop(0)
                        for x in ListofNumbers:
                                print(x)

                        SensorNumber=ListofNumbers[0][18]
                        SensorRange=ListofNumbers[1][15:17]

                        id = 0

                        text_filed = open("FILES/WSN-5d.txt")
                        for x in text_filed:
                                ListofNumbersd.append(x)
                        ListofNumbersd.pop(0)
                        for x in ListofNumbersd:
                                xx = x[0:2]
                                yy = x[5:7]
                                red = random.randint(0, 2)
                                if red == 1:
                                        colo = "red"
                                else:
                                        colo = "green"
                                print(xx + " " + yy)
                                c.create_oval(int(xx) * 4-2, int(yy) * 4-2, int(xx) * 4 + 2,
                                              int(yy) * 4 + 2, stipple="gray50",
                                              outline="green",fill="green", width=1)
                                c.create_oval(int(xx) * 4 - (int(SensorRange)*4),
                                              int(yy) * 4 - (int(SensorRange)*4),
                                              int(xx) * 4 + (int(SensorRange)*4),
                                              int(yy) * 4 + (int(SensorRange)*4),
                                              outline="Green", tags=id)
                                c.create_text(int(xx) * 4 + 15, int(yy) * 4 + 15,
                                              font="Times 10 italic bold", text=id)
                                id += 1;

                        print(SensorNumber + " " + SensorRange)
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

                myButton = tk.Button(main_window, text="COMPLIE", command=Init)
                myButton.pack()
                ExitButton = tk.Button(main_window,text="EXIT",command=Exit)
                ExitButton.pack(side="right")
                SaveButton = tk.Button(main_window, text="Read WSN", command=OpenSensorWSN)
                SaveButton.pack(side="left")
                SaveButton=tk.Button(main_window,text="cal sensor ID",command=SaveFile)
                SaveButton.pack(side="left")
                SaveButton = tk.Button(main_window, text="find WSN graph", command=OpenMYSensorNeighbour)
                SaveButton.pack(side="left")
                main_window.config(menu=menubar)
#########################################################################################################################

        #INSTANCE
        main_window.mainloop()
