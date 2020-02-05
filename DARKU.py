# DarkU
# Created by vincent-coding
# Licences : Apache License 2.0
# START
# !usr/bin/env python
# -*- coding: utf-8 -*-

#Import
import time
from tkinter import *
import tkinter.messagebox
import os
from tcpgecko import *
import sys
from pypresence import Presence

versions = " 1.4.3"

def checkinject():
    ip = wiiuip.get()
    colors = listecouleur.get()
    if ip != "":
        if colors=="Reset":
            wtcp = TCPGecko(ip)
            wtcp.pokemem(0x105DD0A8, 0x3F800000)
            wtcp.s.close()
            tkinter.messagebox.showinfo("DarkU - "+versions, "Injection successful!")
        elif colors=="White":
            wtcp = TCPGecko(ip)
            wtcp.pokemem(0x105DD0A8, 0x40000000)
            wtcp.s.close()
            tkinter.messagebox.showinfo("DarkU - "+versions, "Injection successful!")            
        elif colors=="Black":
            btcp = TCPGecko(ip)
            btcp.pokemem(0x105DD0A8, 0x00000000)
            btcp.s.close()
            tkinter.messagebox.showinfo("DarkU - "+versions, "Injection successful!")
        elif colors=="Light grey":
            lgtcp = TCPGecko(ip)
            lgtcp.pokemem(0x105DD0A8, 0x3E800000)
            lgtcp.s.close()
            tkinter.messagebox.showinfo("DarkU - "+versions, "Injection successful!")  
        elif colors=="Grey":
            gtcp = TCPGecko(ip)
            gtcp.pokemem(0x105DD0A8, 0x3D800000)
            gtcp.s.close()
            tkinter.messagebox.showinfo("DarkU - "+versions, "Injection successful!")
        elif colors=="Dark grey":
            dgtcp = TCPGecko(ip)
            dgtcp.pokemem(0x105DD0A8, 0x3C800000)
            dgtcp.s.close()
            tkinter.messagebox.showinfo("DarkU - "+versions, "Injection successful!")   
        elif colors=="Very dark grey":
            vdgtcp = TCPGecko(ip)
            vdgtcp.pokemem(0x105DD0A8, 0x3B800000)
            vdgtcp.s.close()
            tkinter.messagebox.showinfo("DarkU - "+versions, "Injection successful!")            
    else:
        tkinter.messagebox.showerror("DarkU - "+versions, "Please fill in the \"wiiu ip\" field")
def saveip():
    saveipvalue = wiiuip.get()
    with open("ip.darku", "w") as ipconfig:
        ipconfig.write("ip:"+saveipvalue)
        tkinter.messagebox.showinfo("DarkU - "+versions, "The ip has been saved!")

    
    
client_id = '581046907808382989'
RPC = Presence(client_id)
RPC.connect()
RPC.update(large_image="icons", large_text="DarkU - "+versions, state="By vincent-coding", details="Choose a color")
    
# Interface
main = Tk()

wiiuip = StringVar()
listecouleur = StringVar()
listecouleur.set("Reset")

#Info de la fenetre

main.title("DarkU - "+versions)

#Component
content = Frame(width=250, height=15).pack()
iplabel = Label(content, text="WiiU ip").pack()
ipentry = Entry(content, textvariable=wiiuip).pack()
ipsave = Button(content, text="Save ip",command=saveip).pack(pady=5)
listecolorsmenu = OptionMenu(content, listecouleur, "Reset","White","Light grey", "Grey", "Dark grey", "Very dark grey", "Black").pack(pady=5)
inject = Button(content, text="Inject", command=checkinject).pack(pady=5)

info = Label(main, text="Created by vincent-coding").pack(side=BOTTOM)

try:
    with open('ip.darku'):
        with open('ip.darku') as ipconfig:
            ipconf = ipconfig.readline()
            wiiuip.set(ipconf.replace("ip:",""))
except IOError:
    print("")

main.mainloop()
#Created by vincent-coding
