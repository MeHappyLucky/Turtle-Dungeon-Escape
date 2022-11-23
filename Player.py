# previously named as Turtle class
# renamed to prevent future confusions

class Player:
    """Player's Character"""
    def __init__(self, sight=3.0, speed=1.0):
        self.__sight = sight
        self.__speed = speed

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
