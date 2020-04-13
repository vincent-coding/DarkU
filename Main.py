# DarkU
# Created by vincent-coding
# Licences : Apache License 2.0

# !usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
import sys
import struct
import calendar
import time
from binascii import hexlify
from os import system

class color:
    black       = '\033[98m'
    grey        = '\033[97m'
    cyan        = '\033[96m'
    purple      = '\033[95m'
    blue        = '\033[94m'
    green       = '\033[92m'
    yellow      = '\033[93m'
    red         = '\033[91m'
    white       = '\033[0m'
    bold        = '\033[1m'
    underline   = '\033[4m'


#Variables
version = "2.1"
client_id = '694535619312877598'
adress  = None
wiiuver = None

print("______           _    _   _ ")
print("|  _  \         | |  | | | |")
print("| | | |__ _ _ __| | _| | | |")
print("| | | / _` | '__| |/ / | | |")
print("| |/ / (_| | |  |   <| |_| |")
print("|___/ \__,_|_|  |_|\_\\\___/ ")
print(" By VCoding - Version: " + version)
print("")
if sys.version_info < (3, 0):
    sys.exit(color.red + 'This program only runs on Python 3.')

try:
    from tkinter import *
except:
    sys.exit(color.red + "An error occurred while importing TKinter. Please contact me as soon as possible.")

try:
    from tcpgecko import TCPGecko
    import tkinter.messagebox
except:
    sys.exit(color.red + "An error occurred with the import of pyGecko. Please contact me as soon as possible.")

try:
    from pypresence import Presence
except:
    sys.exit(color.red + "An error occurred while importing PyPresence. Please contact me as soon as possible.")

try:
    RPC = Presence(client_id)
    RPC.connect()
    RPC.update(state="Created by VCoding", details="Uses DarkU " + version, start=calendar.timegm(time.gmtime()), end=None, large_image="icons", large_text="DarkU " + version, small_image="copy", small_text="Created by VCoding", party_id=None, party_size=None)
except:
    print("")

def interface554():
    def saveip():
        saveipvalue = wiiuip.get()
        with open("ip.darku", "w") as ipconfig:
            ipconfig.write("ip:"+saveipvalue)
            tkinter.messagebox.showinfo("DarkU - "+version, "The ip has been saved!")
    
    def inject554():
        ip = wiiuip.get()
        colors = listecouleur.get()
        if ip != "":
            if colors=="Reset":
                tcp = TCPGecko(ip)
                tcp.pokemem(0x105DD2A8, 0x3F800000)
                tcp.s.close()
                tkinter.messagebox.showinfo("DarkU - "+version, "Injection successful!")
            elif colors=="White":
                tcp = TCPGecko(ip)
                tcp.pokemem(0x105DD2A8, 0x40000000)
                tcp.s.close()
                tkinter.messagebox.showinfo("DarkU - "+version, "Injection successful!")            
            elif colors=="Black":
                tcp = TCPGecko(ip)
                tcp.pokemem(0x105DD2A8, 0x00000000)
                tcp.s.close()
                tkinter.messagebox.showinfo("DarkU - "+version, "Injection successful!")
            elif colors=="Light grey":
                tcp = TCPGecko(ip)
                tcp.pokemem(0x105DD2A8, 0x3E800000)
                tcp.s.close()
                tkinter.messagebox.showinfo("DarkU - "+version, "Injection successful!")  
            elif colors=="Grey (Dark Mod)":
                tcp = TCPGecko(ip)
                tcp.pokemem(0x105DD2A8, 0x3D800000)
                tcp.s.close()
                tkinter.messagebox.showinfo("DarkU - "+version, "Injection successful!")
            elif colors=="Dark grey":
                tcp = TCPGecko(ip)
                tcp.pokemem(0x105DD2A8, 0x3C800000)
                tcp.s.close()
                tkinter.messagebox.showinfo("DarkU - "+version, "Injection successful!")   
            elif colors=="Very dark grey":
                tcp = TCPGecko(ip)
                tcp.pokemem(0x105DD2A8, 0x3B800000)
                tcp.s.close()
                tkinter.messagebox.showinfo("DarkU - "+version, "Injection successful!")            
        else:
            tkinter.messagebox.showerror("DarkU - "+version, "Please fill in the \"wiiu ip\" field")

    
    main = Tk()

    wiiuip = StringVar()
    listecouleur = StringVar()
    listecouleur.set("Reset")

    main.title("DarkU " + version + " - By VCoding - V5.5.4")
    main.config(background='#302f2f')
    main.resizable(width = False, height = False)
    width = 300
    height = 220
    wScreen  = main.winfo_screenwidth()
    hScreen  = main.winfo_screenheight()
    x       = (wScreen / 2) - (width / 2)
    y       = (hScreen / 2) - (height / 2)
    main.geometry('%dx%d+%d+%d' % (width, height, x, y))

    iplabel = Label(main, text="WiiU ip",bg='#302f2f', fg='white').pack()
    
    invisible_label = Label(main, text=" ",font=("Arial", 5),background='#302f2f').pack(side=TOP)
    
    ipentry = Entry(main, textvariable=wiiuip, width=26).pack()
    ipsave = Button(main, text="Save ip", width=22 ,command=saveip).pack(pady=5)
    listecolorsmenu = OptionMenu(main, listecouleur, "Reset","White","Light grey", "Grey (Dark Mod)", "Dark grey", "Very dark grey", "Black")
    listecolorsmenu.configure(width=20)
    listecolorsmenu.pack()
    inject = Button(main, text="Inject", command=inject554, width=22).pack(pady=5)

    info = Label(main, text="Created by vincent-coding and TnT GuN",bg='#302f2f', fg='white').pack(side=BOTTOM)

    try:
        with open('ip.darku'):
            with open('ip.darku') as ipconfig:
                ipconf = ipconfig.readline()
                wiiuip.set(ipconf.replace("ip:",""))
    except IOError:
        print("")
    main.mainloop()

def interface55X():
    def saveip():
        saveipvalue = wiiuip.get()
        with open("ip.darku", "w") as ipconfig:
            ipconfig.write("ip:"+saveipvalue)
            tkinter.messagebox.showinfo("DarkU - "+version, "The ip has been saved!")
    
    def inject55X():
        ip = wiiuip.get()
        colors = listecouleur.get()
        if ip != "":
            if colors=="Reset":
                tcp = TCPGecko(ip)
                tcp.pokemem(0x105DD0A8, 0x3F800000)
                tcp.s.close()
                tkinter.messagebox.showinfo("DarkU - "+version, "Injection successful!")
            elif colors=="White":
                tcp = TCPGecko(ip)
                tcp.pokemem(0x105DD0A8, 0x40000000)
                tcp.s.close()
                tkinter.messagebox.showinfo("DarkU - "+version, "Injection successful!")            
            elif colors=="Black":
                tcp = TCPGecko(ip)
                tcp.pokemem(0x105DD0A8, 0x00000000)
                tcp.s.close()
                tkinter.messagebox.showinfo("DarkU - "+version, "Injection successful!")
            elif colors=="Light grey":
                tcp = TCPGecko(ip)
                tcp.pokemem(0x105DD0A8, 0x3E800000)
                tcp.s.close()
                tkinter.messagebox.showinfo("DarkU - "+version, "Injection successful!")  
            elif colors=="Grey (Dark Mod)":
                tcp = TCPGecko(ip)
                tcp.pokemem(0x105DD0A8, 0x3D800000)
                tcp.s.close()
                tkinter.messagebox.showinfo("DarkU - "+version, "Injection successful!")
            elif colors=="Dark grey":
                tcp = TCPGecko(ip)
                tcp.pokemem(0x105DD0A8, 0x3C800000)
                tcp.s.close()
                tkinter.messagebox.showinfo("DarkU - "+version, "Injection successful!")   
            elif colors=="Very dark grey":
                tcp = TCPGecko(ip)
                tcp.pokemem(0x105DD0A8, 0x3B800000)
                tcp.s.close()
                tkinter.messagebox.showinfo("DarkU - "+version, "Injection successful!")            
        else:
            tkinter.messagebox.showerror("DarkU - "+version, "Please fill in the \"wiiu ip\" field")


    main = Tk()

    wiiuip = StringVar()
    listecouleur = StringVar()
    listecouleur.set("Reset")

    main.title("DarkU " + version + " - By VCoding - V5.5.X")
    main.config(background='#302f2f')
    main.resizable(width = False, height = False)
    width = 300
    height = 220
    wScreen  = main.winfo_screenwidth()
    hScreen  = main.winfo_screenheight()
    x       = (wScreen / 2) - (width / 2)
    y       = (hScreen / 2) - (height / 2)
    main.geometry('%dx%d+%d+%d' % (width, height, x, y))

    iplabel = Label(main, text="WiiU ip",bg='#302f2f', fg='white').pack()
    invisible_label = Label(main, text=" ",font=("Arial", 5),background='#302f2f').pack(side=TOP)
    ipentry = Entry(main, textvariable=wiiuip, width=26).pack()
    ipsave = Button(main, text="Save ip", width=22 ,command=saveip).pack(pady=5)
    listecolorsmenu = OptionMenu(main, listecouleur, "Reset","White","Light grey", "Grey (Dark Mod)", "Dark grey", "Very dark grey", "Black")
    listecolorsmenu.configure(width=20)
    listecolorsmenu.pack()
    inject = Button(main, text="Inject", command=inject55X, width=22).pack(pady=5)

    info = Label(main, text="Created by vincent-coding and and TnT GuN",bg='#302f2f', fg='white').pack(side=BOTTOM)
    
    try:
        with open('ip.darku'):
            with open('ip.darku') as ipconfig:
                ipconf = ipconfig.readline()
                wiiuip.set(ipconf.replace("ip:",""))
    except IOError:
        print("")

    main.mainloop()

def validateVer():
    userVersion = selVersion.get()
    if userVersion == "-- Select version --":
        tkinter.messagebox.showerror("DarkU " + version, "Please select a valid version!")
        return
    if userVersion == "5.5.4":
        selectVer.destroy()
        interface554()
        return
    if userVersion == "5.5.3" or userVersion == "5.5.2" or userVersion == "5.5.1":
        selectVer.destroy()
        interface55X()
        return
    



selectVer = Tk()
selectVer.config(background='#302f2f')
selectVer.title("DarkU " + version + " - By VCoding")
selectVer.resizable(width = False, height = False)
width = 350
height = 130
wScreen  = selectVer.winfo_screenwidth()
hScreen  = selectVer.winfo_screenheight()
x       = (wScreen / 2) - (width / 2)
y       = (hScreen / 2) - (height / 2)
selectVer.geometry('%dx%d+%d+%d' % (width, height, x, y))

selVersion = StringVar()
selVersion.set("-- Select version --")

txt = Label(selectVer, text="Select the version of your WiiU.",bg='#302f2f', fg='white').pack()

invisible_label = Label(selectVer, text=" ",font=("Arial", 5),background='#302f2f').pack(side=TOP)

versionList = OptionMenu(selectVer, selVersion, "5.5.4","5.5.3", "5.5.2", "5.5.1")
versionList.configure(width=20)
versionList.pack()
button = Button(selectVer, text="Validated the version", width=22, command=validateVer).pack()
copy = Label(selectVer, text="© 2020 - Software created by VCoding and TnT GuN",bg='#302f2f', fg='white').pack(side=BOTTOM)

tkinter.messagebox.showwarning("DarkU " + version, "Be careful, this version of the software is still a beta. \nAll the software has been redone from scratch, which can cause bugs.\nIf you find a bug, please report it to me on GBATemp or Discord.")

selectVer.mainloop()
