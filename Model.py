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
        :param points: points to add to the score
        :rtype points: int
        """
        self.score += points
        pass

    def get_score(self):
        """
        :return: Getting the score
        """
        return self.score


class Fruits:
    """
    Fruits that will spawn in the game field
    """

    DICT_FRUITS = {"Leaf": 10, "Apple": 100, "Blueberry": 200}

    def __init__(self, ID_fruit, window):
        """
        :param ID_fruit: fruit's ID
        :param window: Surface where fruit appears.

        :rtype ID_fruit: int
        :rtype window: pygame object

        :init fruit: fruit's name
        :init points: points given by this type of fruit
        :init sprite: sprite of the fruit
        :init alive: fruit still eatable
        :init hidden_storage: hidden position to store eaten fruits.

        """
        self.fruit = list(Fruits.DICT_FRUITS.keys())[ID_fruit]
        self.points = list(Fruits.DICT_FRUITS.values())[ID_fruit]

        self.red = ID_fruit % 2
        self.green = max(0, ID_fruit - 2)
        self.blue = max(0, ID_fruit - 1)
        self.sprite = pygame.draw.rect(window, (self.red, self.green, self.blue), (0, 0, 10, 10))

        self.alive = False
        self.hidden_storage = (-50, -50)

    def spawn(self, position):
        """
        Fruit spawning on the field at <position> coordinates.

        :param position: Give the position of a fruit
        :rtype position: tuple
        """
        self.sprite.move(position)
        self.alive = True
        pass

    def eaten(self):
        """
        Fruit eaten by snake, returning to the hidden storage
        """
        self.sprite.move(self.hidden_storage)
        self.alive = False
        pass


class SnakePart:
    """

    """
    def __init__(self, window):
        """
        :param window: Surface where SnakePart appears.
        :rtype window: Pygame object
        """
        self.snake_part = pygame.draw.rect(window, (0, 0, 0) (0, 0, 10, 10))
        self.snake_head  = False
        pass

    def grow(self, position):
        """

        :param position:
        :return:
        """

        pass
