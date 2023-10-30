class Taxicab:
    def __init__(self, x_coord, y_coord):
        self.__x_coord = x_coord
        self.__y_coord = y_coord
        self.__odometer = 0

    def get_x_coord(self):
        return self.__x_coord

    def get_y_coord(self):
        return self.__y_coord

    def get_odometer(self):
        return self.__odometer

    def move_x(self, distance):
        self.__x_coord += distance
        self.__odometer += abs(distance)

    def move_y(self, distance):
        self.__y_coord += distance
        self.__odometer += abs(distance)


cab = Taxicab(5, -8)       # creates a Taxicab object at coordinates (5, -8)
cab.move_x(3)              # moves cab 3 units "right"
cab.move_y(-4)             # moves cab 4 units "down"
cab.move_x(-1)             # moves cab 1 unit "left"
print(cab.get_odometer())  # prints the current odometer reading
# At this point the cab has traveled 3 + 4 + 1 = 8 units and is now at coordinates (7, -12)
