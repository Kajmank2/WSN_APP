# ALL DELETED FILES #
#MENU BAR
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
main_window.config(menu=menubar)

#METHODS
def OpenSernsorId():  # SENSOR ID FILE
    text_file = filedialog.askopenfilename(initialdir="C:/", title="Open TextFile",
                                           filetypes=(("Text Files", "*.txt"),))
    text_file = open(text_file, 'r')
    for x in text_file:
        ListofNumbers.append(x)
    ListofNumbers.pop(0)
    for x in ListofNumbers:
        print(x)
    for x in ListofNumbers:
        xx = x[2:4]
        yy = x[8:10]
        id = x[0]
        red = random.randint(0, 2)
        if red == 1:
            colo = "red"
        else:
            colo = "green"
        print(xx + " " + yy)
        c.create_oval(int(xx) * 4, int(yy) * 4, int(xx) * 4 + 2, int(yy) * 4 + 2, stipple="gray50",
                      fill="green", width=1, tags=id)
        c.create_oval(int(xx) * 4 + 25,
                      int(yy) * 4 + 25,
                      int(xx) * 4 - 25,
                      int(yy) * 4 - 25,
                      fill=colo)
        c.create_text(int(xx) * 4 + 8,
                      int(yy) * 4 + 8,
                      font="Times 10 italic bold", text=id)


def OpenMYSensor():  # SENSOR ID FILE
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
        if (x[3] == '.'):
            xx = [2]
        else:
            xx = x[2:4]
        if (x[9] == '.'):
            yy = x[8]
        else:
            yy = x[8:10]
        id = x[0]
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
    id = 1
    listSens = []
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
        xx = x[0:2]
        yy = x[5:7]

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
        id += 1;
