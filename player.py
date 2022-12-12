
import turtle as tur


class Player:
    """Player's Character"""

    def __init__(self, sight=5.0, speeds=1.8):
        self.__sight = sight
        self.__speed = speeds
        self.__pc = tur.Turtle("circle")
        self.__pc.penup()
        self.__pc.color("white", "#5A5A5A")
        self.__pc.setposition(-40, 20)
        self.__pouch = []

    def level_check(self, level):
        if level != 0:
            self.__sight += self.__sight*level*0.2
            self.__speed += self.__speed*level*0.2

    def moves(self):
        self.__pc.forward(self.__speed)

    @property
    def pouch(self):
        return self.__pouch

    @property
    def sight(self):
        return self.__sight

    @sight.setter
    def sight(self, new_sight):
        self.__sight = new_sight

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, new_speed):
        self.__speed = new_speed

    @property
    def pc(self):
        return self.__pc
