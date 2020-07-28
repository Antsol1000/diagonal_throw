from tkinter import *
import bullet as blt
import matplotlib.pyplot as plt


root = Tk()
root.title("diagonal throw")

label1 = Label(root, text="Please enter the values of parameters.")
label1.grid(row=0, column=1)

label_radius = Label(root, text="Radius of sphere in meters:")
label_radius.grid(row=1, column=0)
radius = Entry(root)
radius.grid(row=1, column=1)

label_angle = Label(root, text="Angle of throw in degrees:")
label_angle.grid(row=2, column=0)
angle = Entry(root)
angle.grid(row=2, column=1)

label_velocity = Label(root, text="Velocity of throw in m/s:")
label_velocity.grid(row=3, column=0)
velocity = Entry(root)
velocity.grid(row=3, column=1)

label_mass = Label(root, text="Mass of bullet in kg:")
label_mass.grid(row=4, column=0)
mass = Entry(root)
mass.grid(row=4, column=1)

radius_value, angle_value, velocity_value, mass_value = 0, 0, 0, 0


def my_click():
    global radius_value, angle_value, velocity_value, mass_value
    radius_value = float(radius.get())
    angle_value = float(angle.get())
    velocity_value = float(velocity.get())
    mass_value = float(mass.get())
    root.destroy()


my_button = Button(root, text="ENTER", command=my_click)
my_button.grid(row=5, column=1)

root.mainloop()


bullet = blt.Bullet(radius_value, mass_value, angle_value, velocity_value)
x, y = [], []


bullet.step()
while bullet.get_y() > 0:
    x.append(bullet.get_x())
    y.append(bullet.get_y())
    bullet.step()

plt.plot(x, y)
x_min, x_max = plt.xlim()
y_min, y_max = plt.ylim()
xy_max = max(x_max, y_max)
plt.xlim(x_min, xy_max)
plt.ylim(y_min, xy_max)
plt.show()
