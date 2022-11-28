
import turtle as tur
import time

class Player:
    """Player's Character"""
    def __init__(self, sight=10.0, speeds=3.0):
        self.__sight = sight
        self.__speed = speeds
        self.__pc = tur.Turtle("turtle")
        self.__pc.color("green")
        self.__pc.penup()

    def moves(self):
        self.__pc.forward(self.__speed)

    def up(self):
        self.__pc.setheading(90)

    def left(self):
        self.__pc.setheading(180)

    def right(self):
        self.__pc.setheading(0)

    def down(self):
        self.__pc.setheading(270)

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
        pass


class Items:
    """to be added to Turtle/Player attributes"""


class Points:
    """(wip) items alt"""


# ===================================== #
# ======= Turtle Dungeon Escape ======= #
# ===================================== #

game_screen = tur.Screen()
game_screen.setup(width=700, height=600)
game_screen.bgcolor("black")
game_screen.title("Turtle Dungeon Escape")
game_screen.tracer(0)

playcha = Player()

game_is_on = True

game_screen.onkey(playcha.up, "Up")
game_screen.onkey(playcha.left, "Left")
game_screen.onkey(playcha.right, "Right")
game_screen.onkey(playcha.down, "Down")
game_screen.listen()

while game_is_on:
    game_screen.update()
    time.sleep(0.1)
    playcha.moves()