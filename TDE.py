
from turtle import *


class Player:
    """Player's Character"""
    def __init__(self, sight=10.0, speeds=6.0):
        self.__sight = sight
        self.__speed = speeds
        self.__pc = Turtle("turtle")
        self.__pc.color("green")
        self.__pc.penup()

    def move_up(self):
        self.__pc.setheading(90)
        self.__pc.forward(self.__speed)

    def move_left(self):
        self.__pc.setheading(180)
        self.__pc.forward(self.__speed)

    def move_right(self):
        self.__pc.setheading(0)
        self.__pc.forward(self.__speed)

    def move_down(self):
        self.__pc.setheading(270)
        self.__pc.forward(self.__speed)

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


class Maps:
    """Generate Maps"""
    def __init__(self):
        self.__screen = Screen()
        self.__screen.setup(width=700, height=600)
        self.__screen.bgcolor("black")
        self.__screen.title("Turtle Dungeon Escape")
        self.__screen.tracer(0)

        game_is_on = True
        while game_is_on:
            self.__screen.update()


class Items:
    """act as a nested dict to be added to Turtle classes' attributes"""


# ===================================== #
# ======= Turtle Dungeon Escape ======= #
# ===================================== #
# print("Welcome to Turtle Dungeon Escape")
# print("press (p) to play")
# print("press (r) to see records")
# print("press (x) to exit")
# menu_prompt = input("What do you want to do?: ")
# if menu_prompt == "p":
    Player()
    Maps()
