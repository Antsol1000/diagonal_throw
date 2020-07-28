"""
class Bullet is used to calculate the diagonal throw of sphere
"""

# imports
import math
import matplotlib.pyplot as plt


# constants

# gravity acceleration
G = 9.81

# time step
DELTA = 0.0001


class Bullet:
    # parameters of throw
    drag_coefficient = 0.47
    radius, mass, angle, velocity = 0, 0, 0, 0
    x, y, v_x, v_y, a_x, a_y = 0, 0, 0, 0, 0, -G
    time = 0

    def __init__(self, radius, mass, angle, velocity):
        """
        :param radius: in meters
        :param mass: in kilograms
        :param angle: in degrees
        :param velocity: in m/s
        """
        self.radius = radius
        self.mass = mass
        self.angle = angle * math.pi / 180
        self.velocity = velocity
        self.air_resistance_factor = 0.5 * 1.2 * math.pi * self.radius ** 2 * self.drag_coefficient
        self.v_x = self.velocity * math.cos(self.angle)
        self.v_y = self.velocity * math.sin(self.angle)

    def step(self):
        """
        change the values of parameters after one step of time
        """
        self.time += DELTA

        self.a_x = -self.air_resistance_factor * self.v_x * abs(self.v_x) / self.mass
        self.a_y = -self.air_resistance_factor * self.v_y * abs(self.v_y) / self.mass - G

        self.v_x += DELTA * self.a_x
        self.v_y += DELTA * self.a_y

        self.x += self.v_x * DELTA
        self.y += self.v_y * DELTA

    def get_time(self):
        """
        :return: time of throw
        """
        return self.time

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
