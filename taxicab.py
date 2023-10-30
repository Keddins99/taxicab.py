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


