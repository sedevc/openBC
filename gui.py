#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import Tkinter as tk
import ttk as ttk
import PIL, tkFont, socket, json, os
from openbccfg import OpenBCcfg
import ConfigParser

REST_SERVER_URL = "http://127.0.0.1:5000"

CFG_PATH = "/cfg/"
CFG_FILE = "openBC.cfg"
CFG = os.path.dirname(os.path.abspath(__file__)) + CFG_PATH + CFG_FILE

OB = OpenBCcfg(CFG) # Read config file.
OB.readConfigFile()

#################################################################
######################### GUI ###################################
#################################################################

def task():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = s.connect_ex(('127.0.0.1',8820))
	if result == 0:
		try:
			result = json.loads(s.recv(1024))
			tTempVar.set(str(result['TANK']) + "℃")
			bTempVar.set(str(int(result['BOILER'])) + "℃")
			fTempVar.set(str(int(result['FIRE'])) + "℃")
			fanRpmVar.set(str(int(result['FAN RPM'])) + "rpm")
			print result
		except:
			pass
	s.close()
	root.after(1000,task)


def GetScaleValues():
	tScaleInt.set(int(OB.TANK_SET_TEMP))
	bScaleInt.set(int(OB.BOILER_SET_TEMP))
	fScaleInt.set(int(OB.FIRE_SET_TEMP))
	lScaleFloat.set(float(OB.LAMBDA_SET_VALUE))

def SetScaleValues():
	config = ConfigParser.RawConfigParser()
	config.set('limits', 'tank_set_temp', '15')
	config.set('limits', 'boiler_set_temp', '40')
	config.set('limits', 'fire_set_temp', '300')
	config.set('limits', 'lambda_set_value', '1.34')
	with open(CFG, 'ab') as configfile:
		config.write(configfile)

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

tScaleInt = IntVar()
bScaleInt = IntVar()
fScaleInt = IntVar()
lScaleFloat = DoubleVar()


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

# ---------- Labels ------------- #
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
# ------------------------------- #

GetScaleValues()

# ---------- Slides ------------- #

tankLabel = Label(settings, font=("Helvetica", 14), text="Tank target ℃")
tankLabel.grid(sticky=SE, row=0, column=0)

tankScale = Scale(settings, variable=tScaleInt, takefocus=0, from_=0, to=100, length=600, width="25", orient=HORIZONTAL)

tankScale.grid(padx=20, pady=0,row=0, column=1)
#########
boilerLabel = Label(settings, font=("Helvetica", 14), text="Boiler target ℃")
boilerLabel.grid(sticky=SE, row=1, column=0)

boilerScale = Scale(settings, variable=bScaleInt, takefocus=0, from_=0, to=100, length=600, width="25", orient=HORIZONTAL)

boilerScale.grid(padx=20, pady=0,row=1, column=1)
##########
fireLabel = Label(settings, font=("Helvetica", 14), text="Fire target ℃")
fireLabel.grid(sticky=SE, row=2, column=0)

fireScale = Scale(settings, variable=fScaleInt, takefocus=0, from_=0, to=800, length=600, width="25", orient=HORIZONTAL)

fireScale.grid(padx=20, pady=0,row=2, column=1)
##########
lambdaLabel = Label(settings, font=("Helvetica", 14), text="Lambda target λ")
lambdaLabel.grid(sticky=SE, row=3, column=0)

lambdaScale = Scale(settings, variable=lScaleFloat, takefocus=0, from_=0.65, to=1.6, resolution=0.02, length=600, width="25", orient=HORIZONTAL)

lambdaScale.grid(padx=20, pady=0,row=3, column=1)


setButton = Button(settings, command=SetScaleValues, text='SET')
#setButton.pack(side='left', anchor='nw', padx=3, pady=5)
setButton.grid(sticky=SE, padx=5, pady=25, row=4, column=0)

setButton = Button(settings, command=GetScaleValues, text='GET')
#setButton.pack(side='left', anchor='nw', padx=3, pady=5)
setButton.grid(sticky=SW, padx=5, pady=25, row=4, column=0)

# ------------------------------- #



root.after(1000,task)



root.mainloop()
