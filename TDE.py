
import time
import csv
from player import *
from map import *
from store import *


# setting facing direction to align with movement
forward_step = 2


def face_up():
    playchar.pc.setheading(90)
    visual.setheading(90)
    playchar.pc.forward(forward_step)


def face_left():
    playchar.pc.setheading(180)
    visual.setheading(180)
    playchar.pc.forward(forward_step)


def face_right():
    playchar.pc.setheading(0)
    visual.setheading(0)
    playchar.pc.forward(forward_step)


def face_down():
    playchar.pc.setheading(270)
    visual.setheading(270)
    playchar.pc.forward(forward_step)


def game_end(txt):
    global run_once
    run_once = 0
    global game_is_on
    game_is_on = "no"
    print("=====================================")
    print(txt)
    print("=====================================")
    main_menu()


def main_menu():
    global game_is_on
    game_is_on = "no"
    print(f"|{'(p) to play':^35}|")
    print(f"|{'(h) for how to play':^35}|")
    print(f"|{'(s) for store':^35}|")
    print(f"|{'(x) to exit':^35}|")
    print("=====================================")
    desire = input('Choose your choice: ')
    if desire not in "phsx":
        print("=====================================")
        print("=== Invalid choice, choose again! ===")
        print("=====================================")
        time.sleep(1)
        main_menu()
    elif desire == "p":
        game_is_on = "yes"
    elif desire == "h":
        with open("game_instructions.txt", "r") as how2:
            read = how2.read().splitlines()
            for i in read:
                print(i)
    elif desire == "s":
        pass
    elif desire == "x":
        pass


def block_collision():
    for blocks in mapp.block_list:
        if playchar.pc.distance(blocks) < 20.5:
            playchar.speed -= playchar.speed
            if playchar.pc.distance(blocks) < 18:
                if playchar.pc.distance(blocks) < 12:
                    game_screen.bye()
                    game_end("==== Turtle Died to Suffocation! ====")
            else:
                playchar.speed = original_speed


# ===================================== #
# ======= Turtle Dungeon Escape ======= #
# ===================================== #

game_is_on = "notyet"
print("=====================================")
print("======= Turtle Dungeon Escape =======")
print("=====================================")
main_menu()
run_once = 0
while game_is_on == "yes":
    if run_once == 0:
        # screen set up
        game_screen = tur.Screen()
        game_screen.setup(width=700, height=600)
        game_screen.bgcolor("black")
        game_screen.title("Turtle Dungeon Escape")
        game_screen.tracer(0)

        # spawning stuffs
        playchar = Player()
        mapp = Maps()

        # place holders
        original_speed = playchar.speed

        # spawn coins
        coin_amount = 15
        for i in range(coin_amount):
            coin = tur.Turtle("circle")
            coin.speed(0)
            coin.penup()
            coin.color("yellow")
            coin.shapesize(stretch_wid=0.5, stretch_len=0.5)
            x = random.randint(-330, 280)
            y = random.randint(-330, 280)
            coin.setposition(x, y)
            playchar.pouch.append(coin)

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

        run_once += 1
    block_collision()
    visual.goto(playchar.pc.pos())
    for coin in playchar.pouch:
        for blocks in mapp.block_list:
            if coin.distance(blocks) < 25 or coin.distance(mapp.exits) < 35:
                x = random.randint(-330, 280)
                y = random.randint(-330, 280)
                coin.goto(x, y)
        coin.hideturtle()
        if coin.distance(playchar.pc) < playchar.sight * 9.85:
            coin.showturtle()
    mapp.exits.hideturtle()
    if mapp.exits.distance(playchar.pc) < playchar.sight * 9.85:
        mapp.exits.showturtle()
    game_screen.update()
    time.sleep(0.000001)
    for coin in playchar.pouch:
        if visual.distance(coin) < 10:
            coin.goto(999, 999)
            coin_collected += 1
            score.clear()
            score.write(f"Coins: {coin_collected}", align="left",
                        font=("Arial", 16, "bold"))
            playchar.pouch.remove(coin)
    if playchar.pc.distance(mapp.exits) < 10:
        game_screen.bye()
        game_end("=======    Turtle Escaped!    =======")
    playchar.moves()
