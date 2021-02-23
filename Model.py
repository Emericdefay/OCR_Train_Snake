import pygame


class Score:
    """
    Contain the score of the game
    """

    def __init__(self):
        """
        :init score: points defining the score
        :rtype score: int
        """
        self.score = 0

    def add_points(self, points):
        """
        DESCRIPTION

        :param points: points to add to the score
        :rtype points: int
        """
        self.score += points
        pass

    def get_score(self):
        """
        DESCRIPTION

        :return: Getting the score
        """
        return self.score


class Fruits:
    """
    Fruits that will spawn in the game field
    """

    DICT_FRUITS = {"Leaf": 10, "Apple": 100, "Blueberry": 200}
    """DICT_FRUITS docstring
    """

    def __init__(self, ID_fruit):
        """
        DESCRIPTION

        :param ID_fruit: fruit's ID

        :rtype ID_fruit: int

        :init fruit: fruit's name
        :init points: points given by this type of fruit


        """
        # Fruit's information
        self.fruit = list(Fruits.DICT_FRUITS.keys())[ID_fruit]
        self.points = list(Fruits.DICT_FRUITS.values())[ID_fruit]

        # Fruit's appearance
        if ID_fruit == 0:
            self.red = 1
            self.green = 0
            self.blue = 0
        if ID_fruit == 1:
            self.red = 0
            self.green = 1
            self.blue = 0
        if ID_fruit == 2:
            self.red = 0
            self.green = 0
            self.blue = 1

        self.color = (self.red*255, self.green*255, self.blue*255)


class SnakePart:
    """
    SnakePart docstring
    """

    SNAKE_ANATOMY = ["head", "neck", "body", "tail"]
    """ SNAKE_ANATOMY docstring
    """

    def __init__(self, snake_part_anatomy):
        """
        DESCRIPTION

        :param snake_part_anatomy:
        :param window: Surface where SnakePart appears.

        :rtype snake_part_anatomy:
        :rtype window: Pygame object
        """

        self.snake_part_anatomy = SnakePart.SNAKE_ANATOMY[snake_part_anatomy]
        self.snake_color = (255, 255, 255)

        pass
