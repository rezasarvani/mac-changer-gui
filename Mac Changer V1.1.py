#!/usr/bin/env python

# Created By Reza Sarvani

from tkinter import *
import subprocess
import os
import re

root = Tk()
root.title("Mac Changer By: Reza Sarvani")
root.geometry('400x300')  # set up the size
color = 'gray55'
root.configure(bg=color)
root.resizable(width=False, height=False)

name_label = Label(root,  font=('arial', 10, 'bold'), text="Reza Sarvani", bg=color, fg="black")
name_label.place(x=0, y=275)



def cmac_get():
	global dinf
	cinf = dinf.get()
	res = subprocess.check_output(["ifconfig", cinf])
	res = str(res)
	fi = re.findall("\w{1,2}:\w{1,2}:\w{1,2}:\w{1,2}:\w{1,2}:\w{1,2}", res)
	for word in fi:
		cmac = fi
	cmac_label2 = Label(root,  font=('arial', 17, 'bold'), text=cmac, bg=color, fg="black")
	cmac_label2.place(x=180, y=75)


def get_inf():
	cm = subprocess.check_output(["ifconfig"])
	cm = str(cm)
	fcm = re.findall(r"(^\w\'\w+\:|\\n\w+\:)", cm)
	return fcm


def change_mac():
	global dinf
	global nmac_entry
	cinf = dinf.get()
	nmac = nmac_entry.get()
	res = subprocess.check_output(["ifconfig", cinf, "down"])
	res = subprocess.check_output(["ifconfig", cinf, "hw", "ether", nmac])
	res = subprocess.check_output(["ifconfig", cinf, "up"])
	suc_msg = Label(root,  font=('arial', 16, 'bold'), text="Mac Address Successfuly Changed!", bg=color, fg="green")
	suc_msg.place(x=10, y=220)

def random_mac():
	global dinf
	cinf = dinf.get()
	res = subprocess.check_output(["ifconfig", cinf, "down"])
	res = subprocess.check_output(["macchanger", "-r", cinf])
	res = subprocess.check_output(["ifconfig", cinf, "up"])
	suc_msg = Label(root,  font=('arial', 16, 'bold'), text="Mac Address Successfuly Changed!", bg=color, fg="green")
	suc_msg.place(x=10, y=220)


inf_label = Label(root,  font=('arial', 20, 'bold'), text="Interface: ", bg=color, fg="white")
inf_label.place(x=10, y=10)

cmac_label = Label(root,  font=('arial', 20, 'bold'), text="Current Mac: ", bg=color, fg="white")
cmac_label.place(x=10, y=70)

nmac_label = Label(root,  font=('arial', 20, 'bold'), text="New Mac: ", bg=color, fg="white")
nmac_label.place(x=10, y=130)

btn_g_mac = Button(root, text="Get Mac", font=('arial', 10, 'bold'),
                  highlightbackground=color,
                  fg="white",
                  command=lambda: cmac_get())
btn_g_mac.place(x=10, y=100)

nmac_entry = Entry(root, bd=7)
nmac_entry.place(x=175,y=130)

btn_n_mac = Button(root, text="Change...", font=('arial', 10, 'bold'),
                  highlightbackground=color,
                  fg="white",
                  command=lambda: change_mac())
btn_n_mac.place(x=10, y=185)

btn_r_mac = Button(root, text="Random Mac Changer", font=('arial', 10, 'bold'),
                  highlightbackground=color,
                  fg="white",
                  command=lambda: random_mac())
btn_r_mac.place(x=110, y=185)

dinf = StringVar(root)
dinf.set("Choose...")
inf_name_f = get_inf()
inf_name = []
for word in inf_name_f:
	inf_name.append(word[2:-1])
inf_drop = OptionMenu(root, dinf, *inf_name)
inf_drop.place(x=210,y=10)


root.mainloop()
