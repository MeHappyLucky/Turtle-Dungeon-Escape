import time
from player import *
from map import *
from level import *

# setting facing direction to align with movement
forward_step = 2

# setting upgrades
upgrade = Level()
player_level = upgrade.level
player_points = upgrade.points
original_level = player_level
original_point = player_points


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


def level_up(level, point):
    global player_level
    global player_points
    global original_level
    global original_point
    original_level = level
    original_point = point
    if level != 0:
        point_required = 20 * level
        if point < point_required:
            player_level = level
            player_points = point
        if point >= point_required:
            player_level = level + 1
            player_points = point - point_required
    else:
        if point < 10:
            return level
        if point >= 10:
            player_level = 1
            player_points -= 10


def game_end(txt):
    global timer
    global run_once
    run_once = 0
    global game_is_on
    game_is_on = "no"
    with open("record.csv", "w") as w:
        w.write(f"{player_level},{player_points}")
    if txt == "exit":
        print("=====================================")
        print("========    Game  Saved      ========")
        print("=====================================")
    else:
        print("=====================================")
        print(txt)
        print("=====================================")
        print(f"|{'Thanks for playing!':^35}|")
        print(f"|{'Your points are saved':^35}|")
        print(f"|{'Play again to use them!':^35}|")
        print("=====================================")


def main_menu():
    global player_level
    global player_points
    global game_is_on
    game_is_on = "no"
    print(f"|{'(p) to play':^35}|")
    print(f"|{'(u) for upgrade':^35}|")
    print(f"|{'(x) to exit':^35}|")
    print("=====================================")
    desire = input('Choose your choice: ')
    if desire not in "phux":
        print("=====================================")
        print("=== Invalid choice, choose again! ===")
        print("=====================================")
        main_menu()
    elif desire == "p":
        game_is_on = "yes"
    elif desire == "u":
        if player_level == 10:
            print("=====================================")
            print("Your Turtle is MAX level! (10)")
            print(f"Your current points is {player_points}")
            print("=====================================")
            print("======= Turtle Dungeon Escape =======")
            print("=====================================")
            main_menu()
        else:
            print("=====================================")
            print("== Upgrade the Turtle with points! ==")
            print("=====================================")
            print(f"Your current points is {player_points}")
            print(f"Your current level is {player_level}")
            wish = input("Do you wish to upgrade? (y/n): ")
            while wish not in "yn":
                print("Please give only y or n (yes or no)...")
                wish = input("Do you wish to upgrade? (y/n): ")
            if wish == "n":
                print("=====================================")
                print("======= Turtle Dungeon Escape =======")
                print("=====================================")
                main_menu()
            else:
                level_up(player_level, player_points)
                if player_level != original_level \
                        and player_points != original_point:
                    print("=====================================")
                    print("=========  Turtle Upgraded! =========")
                    print("=====================================")
                else:
                    print("=====================================")
                    print("! Not enough points, Upgrade Failed !")
                    print("=====================================")
                main_menu()
    elif desire == "x":
        game_end("exit")


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


game_is_on = "yes"
print("=====================================")
print("======= Turtle Dungeon Escape =======")
print("=====================================")
main_menu()
run_once = 0
while game_is_on == "yes":
    try:
        if run_once == 0:
            # screen set up
            game_screen = tur.Screen()
            game_screen.setup(width=700, height=600)
            game_screen.bgcolor("black")
            game_screen.title("Turtle Dungeon Escape")
            game_screen.tracer(0)

            # spawning stuffs
            playchar = Player()
            playchar.level_check(player_level)
            playchar.pc.shapesize(stretch_wid=playchar.sight,
                                  stretch_len=playchar.sight)
            mapp = Maps()
            for point in mapp.points_list:
                playchar.pouch.append(point)

            # place holders
            original_speed = playchar.speed

            # points collection
            score = tur.Turtle()
            score.speed(0)
            score.color("green")
            score.penup()
            score.goto(-335, 270)
            score.pendown()
            score.write(f"Points: {player_points}", align="left",
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

            # exit
            if mapp.exits.distance(visual) < 250:
                x = random.randint(-330, 280)
                y = random.randint(-330, 280)
                mapp.exits.goto(x, y)

            run_once = 1

        if playchar.pc.distance(mapp.exits) < 10:
            game_screen.bye()
            player_points += 15
            game_end("==== Turtle Escaped (+15 points) ====")
        block_collision()
        score.clear()
        score.write(f"Points: {player_points}", align="left",
                    font=("Arial", 16, "bold"))
        visual.goto(playchar.pc.pos())
        for point in playchar.pouch:
            for blocks in mapp.block_list:
                if point.distance(blocks) < 35 or point.distance(
                        mapp.exits) < 35:
                    x = random.randint(-330, 280)
                    y = random.randint(-330, 280)
                    point.goto(x, y)
            point.hideturtle()
            if point.distance(playchar.pc) < playchar.sight * 9.85:
                point.showturtle()
        for blocks in mapp.block_list:
            if mapp.exits.distance(blocks) < 30:
                x = random.randint(-330, 280)
                y = random.randint(-330, 280)
                mapp.exits.goto(x, y)
        mapp.exits.hideturtle()
        if mapp.exits.distance(playchar.pc) < playchar.sight * 9.85:
            mapp.exits.showturtle()
        game_screen.update()
        time.sleep(0.000001)
        for point in playchar.pouch:
            if visual.distance(point) < 10:
                point.goto(999, 999)
                player_points += 1
                score.clear()
                score.write(f"Points: {player_points}", align="left",
                            font=("Arial", 16, "bold"))
                playchar.pouch.remove(point)
        playchar.moves()
    except:
        game_end("exit")
