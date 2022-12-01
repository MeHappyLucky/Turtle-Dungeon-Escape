import turtle as tur
import time
import random


class Player:
    """Player's Character"""

    def __init__(self, sight=30.0, speeds=1.2):
        self.__sight = sight
        self.__speed = speeds
        self.__pc = tur.Turtle("circle")
        self.__pc.color("white", "#5A5A5A")
        self.__pc.setposition(0, 0)
        self.__pc.shapesize(stretch_wid=self.sight, stretch_len=self.sight)
        self.__pc.penup()
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


class Maps:
    """Generate map related stuffs"""

    def __init__(self):
        self.get_map()
        llist = [(150, -160), (180, -190), (-200, 160), (170, -130),
                 (-120, 200), (-100, 110), (110, -200), (130, -150)]
        exits = tur.Turtle("square")
        exits.penup()
        exits.color("red")
        rng = random.randrange(0, 7)
        exits.setposition(llist[rng])
        self.__exits = exits

    @property
    def exits(self):
        return self.__exits

    def get_map(self):
        pass


class Store:
    """sells items"""


# setting facing direction to align with movement
forward_step = 2


def face_up():
    playcha.pc.setheading(90)
    visual.setheading(90)
    playcha.pc.forward(forward_step)


def face_left():
    playcha.pc.setheading(180)
    visual.setheading(180)
    playcha.pc.forward(forward_step)


def face_right():
    playcha.pc.setheading(0)
    visual.setheading(0)
    playcha.pc.forward(forward_step)


def face_down():
    playcha.pc.setheading(270)
    visual.setheading(270)
    playcha.pc.forward(forward_step)


def game_end(txt, color, font, size):
    for coin in playcha.pouch:
        coin.goto(999, 999)
    mapp.exits.goto(999, 999)
    playcha.pc.goto(-999, 999)
    ending = tur.Turtle()
    ending.speed(0)
    ending.color(f"{color}")
    ending.penup()
    ending.goto(0, 150)
    ending.pendown()
    ending.write(f"{txt}", align="center",
                 font=(f"{font}", size, "normal"))
    ending.color("white")
    ending.penup()
    ending.goto(0, 80)
    ending.pendown()
    ending.write("(m) back to menu", align="center",
                 font=("Arial", 24, "normal"))
    ending.penup()
    ending.goto(0, 30)
    ending.pendown()
    ending.write("(p) play again", align="center",
                 font=("Arial", 24, "normal"))
    ending.penup()
    ending.goto(0, -20)
    ending.pendown()
    ending.write("(x) exit", align="center",
                 font=("Arial", 24, "normal"))
    ending.hideturtle()
    playcha.speed = 0


# ===================================== #
# ======= Turtle Dungeon Escape ======= #
# ===================================== #


# screen set up
game_screen = tur.Screen()
game_screen.setup(width=700, height=600)
game_screen.bgcolor("black")
game_screen.title("Turtle Dungeon Escape")
game_screen.tracer(0)

# spawning stuffs
playcha = Player()
mapp = Maps()

# place holders
original_speed = playcha.speed

# spawn coins
for i in range(20):
    coin = tur.Turtle("circle")
    coin.speed(0)
    coin.penup()
    coin.color("yellow")
    coin.shapesize(stretch_wid=0.5, stretch_len=0.5)
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    coin.setposition(x, y)
    playcha.pouch.append(coin)

# coins collection
coin_collected = 0

score = tur.Turtle()
score.speed(0)
score.color("green")
score.penup()
score.goto(-335, 270)
score.pendown()
score.write(f"Coins: {coin_collected}", align="left",
            font=("Arial", 16, "bold"))
score.hideturtle()

# visual turtle
visual = tur.Turtle("turtle")
visual.speed(0)
visual.penup()
visual.color("black", "green")

# movement
game_screen.onkey(face_up, "Up")
game_screen.onkey(face_left, "Left")
game_screen.onkey(face_right, "Right")
game_screen.onkey(face_down, "Down")
game_screen.listen()

# BLOCK
block_positions = [(100,100),(100,130)]
block_list = []
for positions in block_positions:
    block = tur.Turtle("square")
    block.color("black")
    block.speed(0)
    block.penup()
    block.setposition(positions)
    block.shapesize(stretch_wid=1, stretch_len=1)
    block_list.append(block)

# Game Main part
while True:
    for block in block_list:
        if block.distance(visual) < 18:
            playcha.speed = 0
            if block.distance(visual) < 11:
                game_end("Turtle Died to Suffocation!", "red", "Arial", 40)
        else:
            playcha.speed = original_speed
    visual.goto(playcha.pc.pos())
    for coin in playcha.pouch:
        coin.hideturtle()
        if coin.distance(playcha.pc) < playcha.sight * 9.85:
            coin.showturtle()
    game_screen.update()
    time.sleep(0.0001)
    for coin in playcha.pouch:
        if visual.distance(coin) < 10:
            coin.goto(999, 999)
            coin_collected += 1
            score.clear()
            score.write(f"Coins: {coin_collected}", align="left",
                        font=("Arial", 16, "bold"))
            playcha.pouch.remove(coin)
    if playcha.pc.distance(mapp.exits) < 10:
        game_end("Turtle Escaped!", "blue", "Arial", 40)
    playcha.moves()
