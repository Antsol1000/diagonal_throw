from tkinter import *
import os
import matplotlib.pyplot as plt


root = Tk()
root.title("diagonal throw")

label1 = Label(root, text="Please enter the values of parameters.")
label1.grid(row=0, column=1)

label_angle = Label(root, text="Angle of throw in degrees:")
label_angle.grid(row=1, column=0)
angle = Entry(root)
angle.grid(row=1, column=1)

label_velocity = Label(root, text="Velocity of throw in m/s:")
label_velocity.grid(row=2, column=0)
velocity = Entry(root)
velocity.grid(row=2, column=1)

label_mass = Label(root, text="Mass of bullet in kg:")
label_mass.grid(row=3, column=0)
mass = Entry(root)
mass.grid(row=3, column=1)


def my_click():
    global param
    param = angle.get() + " " + velocity.get() + " " + mass.get()
    root.destroy()


my_button = Button(root, text="ENTER", command=my_click)
my_button.grid(row=4, column=1)

root.mainloop()

os.system("main.exe " + param)

while open("wyniki.txt") == -1:
    1 == 1

x = []
y = []
file = open("wyniki.txt", 'r')
for line in file:
    temp = line.split(" ")
    x.append(float(temp[0]))
    y.append(float(temp[1]))
file.close()

plt.plot(x, y)
xmin, xmax = plt.xlim()
ymin, ymax = plt.ylim()
xymax = max(xmax, ymax)
plt.xlim(xmin, xymax)
plt.ylim(ymin, xymax)
plt.show()

os.system("del wyniki.txt")
