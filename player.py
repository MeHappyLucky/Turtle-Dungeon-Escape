
import turtle as tur


class Player:
    """Player's Character"""

    def __init__(self, sight=40.0, speeds=2):
        self.__sight = sight
        self.__speed = speeds
        self.__pc = tur.Turtle("circle")
        self.__pc.penup()
        self.__pc.color("white", "#5A5A5A")
        self.__pc.setposition(0, 0)
        self.__pc.shapesize(stretch_wid=self.sight, stretch_len=self.sight)
        self.__pouch = []
        self.__bought = []

    def equip(self):
        for items in self.__bought:
            for stat in items.values():
                self.__sight += stat[0]
                self.__speed += stat[1]

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
