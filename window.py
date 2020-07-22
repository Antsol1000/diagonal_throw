from tkinter import *
import os
import matplotlib.pyplot as plot


root = Tk()

angle = Entry(root)
velocity = Entry(root)
mass = Entry(root)
angle.grid(row=0, column=0)
velocity.grid(row=0, column=1)
mass.grid(row=0, column=2)
angle.insert(0, "angle")
velocity.insert(0, "velocity")
mass.insert(0, "mass")


def my_click():
    global param
    param = angle.get() + " " + velocity.get() + " " + mass.get()
    root.destroy()


my_button = Button(root, text="ENTER", command=my_click)
my_button.grid(row=1, column=1)

root.mainloop()

os.system("C:\\Users\\antso\\Desktop\\diagonal_throw\\main.exe " + param)

x = []
y = []
file = open("wyniki.txt", 'r')
for line in file:
    temp = line.split(" ")
    x.append(float(temp[0]))
    y.append(float(temp[1]))
file.close()

plot.plot(x, y)
plot.show()
