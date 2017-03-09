#!/usr/bin/env python3

from tkinter import (Tk, Label, Checkbutton, Entry, E, W, SUNKEN,
                     IntVar, StringVar, Button)
import time
import csv

# initializing Tkinter
root = Tk()

# setting window title
root.wm_title("MiSeq Wartungsstatus")


# creating a .csv file to save the status of each step including the date
def wash_status():
    with open("status.csv", "w", newline="") as csvfile:
        cw = csv.writer(csvfile, delimiter=",")
        cw.writerow(["check_postw", check_postw.get()])
        cw.writerow(["entry_postw", entry_postw.get()])
        cw.writerow(["check_mainw1", check_mainw1.get()])
        cw.writerow(["entry_mainw1", entry_mainw1.get()])
        cw.writerow(["check_mainw2", check_mainw2.get()])
        cw.writerow(["entry_mainw2", entry_mainw2.get()])
        cw.writerow(["check_mainw3", check_mainw3.get()])
        cw.writerow(["entry_mainw3", entry_mainw3.get()])
        cw.writerow(["check_restart", check_restart.get()])
        cw.writerow(["entry_restart", entry_restart.get()])
        cw.writerow(["check_mainw4", check_mainw4.get()])
        cw.writerow(["entry_mainw4", entry_mainw4.get()])
        cw.writerow(["check_mainw5", check_mainw5.get()])
        cw.writerow(["entry_mainw5", entry_mainw5.get()])
        cw.writerow(["check_mainw6", check_mainw6.get()])
        cw.writerow(["entry_mainw6", entry_mainw6.get()])
        cw.writerow(["current_status", current_status.get()])


# reading the .csv file to restore the saved statuses and dates
def load_wash_status():
    with open("status.csv") as csvfile:
        reader = csv.reader(csvfile)
        mydict = dict((rows[0], rows[1]) for rows in reader)
        check_postw.set(mydict["check_postw"])
        entry_postw.set(mydict["entry_postw"])
        check_mainw1.set(mydict["check_mainw1"])
        entry_mainw1.set(mydict["entry_mainw1"])
        check_mainw2.set(mydict["check_mainw2"])
        entry_mainw2.set(mydict["entry_mainw2"])
        check_mainw3.set(mydict["check_mainw3"])
        entry_mainw3.set(mydict["entry_mainw3"])
        check_restart.set(mydict["check_restart"])
        entry_restart.set(mydict["entry_restart"])
        check_mainw4.set(mydict["check_mainw4"])
        entry_mainw4.set(mydict["entry_mainw4"])
        check_mainw5.set(mydict["check_mainw5"])
        entry_mainw5.set(mydict["entry_mainw5"])
        check_mainw6.set(mydict["check_mainw6"])
        entry_mainw6.set(mydict["entry_mainw6"])
        current_status.set(mydict["current_status"])


# resetting all checkbuttons and entry widgets
def reset_status():
    check_postw.set(0)
    entry_postw.set("")
    check_mainw1.set(0)
    entry_mainw1.set("")
    check_mainw2.set(0)
    entry_mainw2.set("")
    check_mainw3.set(0)
    entry_mainw3.set("")
    check_restart.set(0)
    entry_restart.set("")
    check_mainw4.set(0)
    entry_mainw4.set("")
    check_mainw5.set(0)
    entry_mainw5.set("")
    check_mainw6.set(0)
    entry_mainw6.set("")
    current_status.set(" nicht bereit")


# set value of entry widgets to the current date when the checkbuttons are on
def set_date_postw():
    current_date = time.strftime("%d.%m.%y")
    if check_postw.get() == 1:
        entry_postw.set(current_date)
    else:
        entry_postw.set("")


def set_date_mainw1():
    current_date = time.strftime("%d.%m.%y")
    if check_mainw1.get() == 1:
        entry_mainw1.set(current_date)
    else:
        entry_mainw1.set("")


def set_date_mainw2():
    current_date = time.strftime("%d.%m.%y")
    if check_mainw2.get() == 1:
        entry_mainw2.set(current_date)
    else:
        entry_mainw2.set("")


def set_date_mainw3():
    current_date = time.strftime("%d.%m.%y")
    if check_mainw3.get() == 1:
        entry_mainw3.set(current_date)
    else:
        entry_mainw3.set("")


def set_date_restart():
    current_date = time.strftime("%d.%m.%y")
    if check_restart.get() == 1:
        entry_restart.set(current_date)
    else:
        entry_restart.set("")


def set_date_mainw4():
    current_date = time.strftime("%d.%m.%y")
    if check_mainw4.get() == 1:
        entry_mainw4.set(current_date)
    else:
        entry_mainw4.set("")


def set_date_mainw5():
    current_date = time.strftime("%d.%m.%y")
    if check_mainw5.get() == 1:
        entry_mainw5.set(current_date)
    else:
        entry_mainw5.set("")


def set_date_mainw6():
    current_date = time.strftime("%d.%m.%y")
    if check_mainw6.get() == 1:
        entry_mainw6.set(current_date)
        current_status.set(" bereit")
    else:
        entry_mainw6.set("")
        current_status.set(" nicht bereit")


# setup Tkinter GUI
Label(root, text="Datum").grid(row=0, column=3, pady=4)

Label(root, text="Post-run Wash (1 x 30 min)").grid(row=1, sticky=E, padx=2, pady=2)
check_postw = IntVar()
Checkbutton(root, variable=check_postw, command=set_date_postw).grid(row=1, column=2)
entry_postw = StringVar()
Entry(root, textvariable=entry_postw, width=8).grid(row=1, column=3)

Label(root, text="Maintenance Wash (3 x 20 min)").grid(row=2, sticky=E, padx=2, pady=2)
Label(root, text="1st").grid(row=2, column=1, sticky=E, padx=2, pady=2)
check_mainw1 = IntVar()
Checkbutton(root, variable=check_mainw1, command=set_date_mainw1).grid(row=2, column=2)
entry_mainw1 = StringVar()
Entry(root, textvariable=entry_mainw1, width=8).grid(row=2, column=3)

Label(root, text="2nd").grid(row=3, column=1, sticky=E, padx=2, pady=2)
check_mainw2 = IntVar()
Checkbutton(root, variable=check_mainw2, command=set_date_mainw2).grid(row=3, column=2)
entry_mainw2 = StringVar()
Entry(root, textvariable=entry_mainw2, width=8).grid(row=3, column=3)

Label(root, text="3rd").grid(row=4, column=1, sticky=E, padx=2, pady=2)
check_mainw3 = IntVar()
Checkbutton(root, variable=check_mainw3, command=set_date_mainw3).grid(row=4, column=2)
entry_mainw3 = StringVar()
Entry(root, textvariable=entry_mainw3, width=8).grid(row=4, column=3)

Label(root, text="Restart MiSeq").grid(row=5, sticky=E, padx=2, pady=2)
check_restart = IntVar()
Checkbutton(root, variable=check_restart, command=set_date_restart).grid(row=5, column=2)
entry_restart = StringVar()
Entry(root, textvariable=entry_restart, width=8).grid(row=5, column=3)

Label(root, text="Maintenance Wash (3 x 20 min)").grid(row=6, sticky=E, padx=2, pady=2)
Label(root, text="1st").grid(row=6, column=1, sticky=E, padx=2, pady=2)
check_mainw4 = IntVar()
Checkbutton(root, variable=check_mainw4, command=set_date_mainw4).grid(row=6, column=2)
entry_mainw4 = StringVar()
Entry(root, textvariable=entry_mainw4, width=8).grid(row=6, column=3)

Label(root, text="2nd").grid(row=7, column=1, sticky=E, padx=2, pady=2)
check_mainw5 = IntVar()
Checkbutton(root, variable=check_mainw5, command=set_date_mainw5).grid(row=7, column=2)
entry_mainw5 = StringVar()
Entry(root, textvariable=entry_mainw5, width=8).grid(row=7, column=3)

Label(root, text="3rd").grid(row=8, column=1, sticky=E, padx=2, pady=2)
check_mainw6 = IntVar()
Checkbutton(root, variable=check_mainw6, command=set_date_mainw6).grid(row=8, column=2)
entry_mainw6 = StringVar()
Entry(root, textvariable=entry_mainw6, width=8).grid(row=8, column=3)

Button(root, text="Speichern", command=wash_status).grid(row=9, column=0, sticky=E, pady=4)
Button(root, text="Laden", command=load_wash_status).grid(row=9, column=1, pady=4)
Button(root, text="Zurücksetzen", command=reset_status).grid(row=9, column=2, columnspan=2, pady=4)

current_status = StringVar()
current_status.set(" nicht bereit")
Label(root, textvariable=current_status, bd=1, relief=SUNKEN, anchor=W).grid(columnspan=4, sticky=W+E)

# Tkinter event loop
root.mainloop()
