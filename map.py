import csv
import random
import turtle as tur


class Maps:
    """Generate map related stuffs"""

    def __init__(self):
        exits = tur.Turtle("square")
        exits.penup()
        exits.color("red")
        x = random.randint(-330, 280)
        y = random.randint(-330, 280)
        exits.setposition(x, y)
        self.__exits = exits
        self.__block_list = []
        self.__block_positions = []
        self.__points_list = []
        self.get_map()
        self.spawn_points()

    def spawn_points(self):
        for i in range(15):
            point = tur.Turtle("circle")
            point.speed(0)
            point.penup()
            point.color("yellow")
            point.shapesize(stretch_wid=0.5, stretch_len=0.5)
            x = random.randint(-330, 280)
            y = random.randint(-330, 280)
            point.setposition(x, y)
            self.__points_list.append(point)

    @property
    def points_list(self):
        return self.__points_list

    @property
    def block_list(self):
        return self.__block_list

    @property
    def block_positions(self):
        return self.__block_positions

    @property
    def exits(self):
        return self.__exits

    def get_map(self):
        with open("maps_data.csv", "r") as maps_data:
            map_gen = csv.reader(maps_data)
            llist = list(map_gen)
            for i in range(len(llist)):
                if llist[i] != ["x", "y"]:
                    j = float(llist[i][0])
                    k = float(llist[i][1])
                    self.__block_positions.append((j, k))

        for positions in self.__block_positions:
            block = tur.Turtle("square")
            block.color("black")
            block.speed(0)
            block.penup()
            block.setposition(positions)
            block.shapesize(stretch_wid=1, stretch_len=1)
            self.__block_list.append(block)
