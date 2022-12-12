import csv


class Level:
    """sell items"""
    def __init__(self):
        self.__points, self.__level = self.read_points()

    def read_points(self):
        with open("record.csv", "r") as r:
            read = csv.reader(r)
            llist = []
            for i in read:
                for j in i:
                    llist.append(int(j))
            if llist[0] > 10:
                llist[0] = 10
            return llist[1], llist[0]

    @property
    def points(self):
        return self.__points

    @property
    def level(self):
        return self.__level
