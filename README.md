# Turtle Dungeon Escape

Turtle Dungeon Escape is a game where you will be playing as a turtle escaping a dungeon (a maze). The goal of the game is to collect points, in the game you can find points lying around where you should be able to collect them. You can also earn points fast by finding the exit. With these points you can upgrade your turtle to the next level, doing so will help you earn points at a faster pace.

This game should consist of 4 .py file and 2 .csv files.
* Turtle Dungeon Escape.py
* player.py
* map.py
* level.py
* maps_data.csv
* records.csv

**Turtle Dungeon Escape.py is the main file to run if you want to play the game.**

Turtle Dungeon Escape.py imports time and * from the other .py files.\
player.py imports turtle.\
map.py imports turtle, random, csv\
level.py imports csv

player.py, previously named as turtle.py, changed to prevent a possible misleading name.\
player.py contains the Player class. It controls the level of the turtle to be as intended. It also controls the vision and moves the player character by the speed of the turtle relative to the level.

map.py is there to generate the important elements of the game, which are, points and exit and also the dungeon / maze itself.
 It reads the maps_data.csv file which contains the information about the dungeon's structure.

level.py is there to read the level of the player's character, the turtle, and the accumulated points. It reads from the record.csv file which contain the said information. It stores the information to give when it is called to do so.


\
\
\
\
This game is made by Sukprachoke Leelapisuth. \
Purposed to be the final project for semester 1 in Programming 1 class of the faculty of software and knowledge engineering at Kasetsart University.