#!/usr/bin/python3

# --------------------------------------- #
# Program Author: ?????
# Date of Creation: 06/22/22
# Last Modified: 07/07/22
# Function: Display Voltage Data to GUI
# Comments: Test Program
# ---------------------------------------- #

# Importing GUI packages
from tkinter import *
from spiRead import *

root = Tk()
root.geometry("800x480")
root.title(" ")
root.configure(bg='light blue')

voltage = spiRead.voltage

channel1Label = Label(root, text="0", font=("Calibre", 60), width=7, borderwidth=3, relief="solid")
channel1Label.place(x=10, y=20)

root.mainloop()
