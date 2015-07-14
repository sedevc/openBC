#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import Tkinter as tk
import ttk as ttk
import PIL, tkFont, socket, json, os, urllib, ConfigParser
from time import gmtime, strftime
from openbccfg import OpenBCcfg



REST_SERVER_URL = "http://127.0.0.1:8080/api/status"

CFG_PATH = "/cfg/"
CFG_FILE = "openBC.cfg"
CFG = os.path.dirname(os.path.abspath(__file__)) + CFG_PATH + CFG_FILE


OB = OpenBCcfg(CFG) 
#################################################################
######################### GUI ###################################
#################################################################

def task():
	try:
		response = urllib.urlopen(REST_SERVER_URL);
		result = json.loads(response.read())
		tTempVar.set(str(result['TANK']) + "℃")
		bTempVar.set(str(int(result['BOILER'])) + "℃")
		fTempVar.set(str(int(result['FIRE'])) + "℃")
		fanRpmVar.set(str(int(result['FAN RPM'])) + "rpm")
		serverStatusVar.set("ONLINE")
		print result
	except:
		serverStatusVar.set("OFFLINE")
	timeStatusVar.set(str(strftime("%Y-%m-%d %H:%M:%S", gmtime())))
	root.after(1000,task)


def GetScaleValues():
	
	OB.readConfigFile()
	tScaleInt.set(int(OB.TANK_SET_TEMP))
	bScaleInt.set(int(OB.BOILER_SET_TEMP))
	fScaleInt.set(int(OB.FIRE_SET_TEMP))
	lScaleFloat.set(float(OB.LAMBDA_SET_VALUE))
	blockTimeInt.set(int(OB.BLOCK_TIME))
	screwRuntimeInt.set(int(OB.RUN_TIME_SCREW))

def SetScaleValues():
	OB.TANK_SET_TEMP = str(tScaleInt.get())
	OB.BOILER_SET_TEMP = str(bScaleInt.get())
	OB.FIRE_SET_TEMP = str(fScaleInt.get())
	OB.LAMBDA_SET_VALUE = str(lScaleFloat.get())
	OB.BLOCK_TIME  = str(blockTimeInt.get())
	OB.RUN_TIME_SCREW = str(screwRuntimeInt.get())
	OB.WriteConfigFile()

# ----------- GUI ROOT ------------ #

root = tk.Tk()
root.geometry("%dx%d" % (800, 480))
root.title('Autoburner V0.1')
#root.overrideredirect(1)
# -------------------------------- #

tTempVar = StringVar()
bTempVar = StringVar()
fTempVar = StringVar()
fanRpmVar = StringVar()
timeStatusVar = StringVar()
serverStatusVar = StringVar()
timeStatusVar.set(str(strftime("%Y-%m-%d %H:%M:%S", gmtime())))



tScaleInt = IntVar()
bScaleInt = IntVar()
fScaleInt = IntVar()
lScaleFloat = DoubleVar()
blockTimeInt = IntVar()
screwRuntimeInt = IntVar()


tTempVar.set(0)
bTempVar.set(0)
fTempVar.set(0)
fanRpmVar.set(0)

# ------------ Font --------------- #
f = tkFont.Font(family='helvetica', size=-16)
s = ttk.Style()
s.configure('.', font=f)
# --------------------------------- #

# ---------- Notebook ------------ #
nb = ttk.Notebook(root)
nb.pack(fill='both', expand='yes')
# create a child frame for each page
status = tk.Frame()
settings = tk.Frame()#bg='blue')
log = tk.Frame()

# create the pages
nb.add(status, text='Status')
nb.add(settings, text='Settings')
nb.add(log, text='Log')
# -------------------------------- #

# ---------- BACKGROUND ---------- #
background_image = PhotoImage(file=os.path.dirname(os.path.abspath(__file__)) + "/boiler.gif")
background_label = Label(status, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
# ------------------------------- #

# ℃


# ---------- Status ------------- #
#serverStatus = Label(status, textvariable=serverStatusVar, fg="black", font=("Helvetica", 12))
#serverStatus.place(x=700, y=0)

tTempLabel = Label(status, textvariable=tTempVar, fg="black", font=("Helvetica", 16))
tTempLabel.place(x=103, y=120)

bTempLabel = Label(status, textvariable=bTempVar, fg="black", font=("Helvetica", 16))
bTempLabel.place(x=360, y=150)

fTempLabel = Label(status, textvariable=fTempVar, fg="red", font=("Helvetica", 16))
fTempLabel.place(x=500, y=310)

LambdaLabel = Label(status, text="1.4λ", fg="black", font=("Helvetica", 16))
LambdaLabel.place(x=265, y=146)

FanLabel = Label(status, textvariable=fanRpmVar, fg="black", font=("Helvetica", 12))
FanLabel.place(x=510, y=190)

statusBar = Label(status, bd=1, relief=SUNKEN, anchor=W, font=("Helvetica", 10))
statusBar.pack(side=BOTTOM ,fill=X)

timeStatus = Label(statusBar, textvariable=timeStatusVar, bd=1, relief=SUNKEN, anchor=W, font=("Helvetica", 10))
timeStatus.pack(side=LEFT)

serverStatus = Label(statusBar, textvariable=serverStatusVar, bd=1, relief=SUNKEN, anchor=W, font=("Helvetica", 10))
serverStatus.pack(side=RIGHT)

# ------------------------------- #

GetScaleValues()

# ---------- Settings ------------- #

tankLabel = Label(settings, font=("Helvetica", 13), text="Tank target ℃")
tankLabel.grid(sticky=SE, row=0, column=0)
tankScale = Scale(settings, variable=tScaleInt, takefocus=0, from_=0, to=100, length=600, width="25", orient=HORIZONTAL)
tankScale.grid(padx=20, pady=0,row=0, column=1)
#########
boilerLabel = Label(settings, font=("Helvetica", 13), text="Boiler target ℃")
boilerLabel.grid(sticky=SE, row=1, column=0)
boilerScale = Scale(settings, variable=bScaleInt, takefocus=0, from_=0, to=100, length=600, width="25", orient=HORIZONTAL)
boilerScale.grid(padx=20, pady=0,row=1, column=1)
##########
fireLabel = Label(settings, font=("Helvetica", 13), text="Fire target ℃")
fireLabel.grid(sticky=SE, row=2, column=0)
fireScale = Scale(settings, variable=fScaleInt, takefocus=0, from_=0, to=800, length=600, width="25", orient=HORIZONTAL)
fireScale.grid(padx=20, pady=0,row=2, column=1)
##########
lambdaLabel = Label(settings, font=("Helvetica", 13), text="Lambda target λ")
lambdaLabel.grid(sticky=SE, row=3, column=0)
lambdaScale = Scale(settings, variable=lScaleFloat, takefocus=0, from_=0.65, to=1.6, resolution=0.02, length=600, width="25", orient=HORIZONTAL)
lambdaScale.grid(padx=20, pady=0,row=3, column=1)
##########
blockTimeLabel = Label(settings, font=("Helvetica", 13), text="Block time screw(s)")
blockTimeLabel.grid(sticky=SE, row=4, column=0)
blockTimeScale = Scale(settings, variable=blockTimeInt, takefocus=0, from_=0, to=800, length=600, width="25", orient=HORIZONTAL)
blockTimeScale.grid(padx=20, pady=0,row=4, column=1)
###########
screwRuntimeLabel = Label(settings, font=("Helvetica", 13), text="Screw run time(s)")
screwRuntimeLabel.grid(sticky=SE, row=5, column=0)
screwRuntimeScale = Scale(settings, variable=screwRuntimeInt, takefocus=0, from_=0, to=20, length=600, width="25", orient=HORIZONTAL)
screwRuntimeScale.grid(padx=20, pady=0,row=5, column=1)
###########
setButton = Button(settings, command=SetScaleValues, text='Set')
setButton.grid(sticky=SE, padx=5, pady=25, row=6, column=0)
##########
setButton = Button(settings, command=GetScaleValues, text='Undo')
setButton.grid(sticky=SW, padx=5, pady=25, row=6, column=0)
# ------------------------------- #



root.after(1000,task)



root.mainloop()
