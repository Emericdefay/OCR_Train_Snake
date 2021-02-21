import pygame


class GameWindow:
    """

    """
    WIDTH = 862
    HEIGHT = 862
    """
    """

    def __init__(self):
        """

        """
        pygame.init()
        self.window = pygame.display.set_mode((GameWindow.WIDTH, GameWindow.HEIGHT))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()

        self.window.fill((0, 0, 0))

        self.size_pixel = 25

        self.pixel = pygame.draw.rect(self.window, (0, 0, 0), (0, 0, 0, 0))

        self.matrix_field = [[1 for i in range(32)] for j in range(32)]
        self.position_x = 0
        self.position_y = 0

        self.field_color = (10, 10, 10)

        pass

    def pixel_draw(self, position_x, position_y, color):
        """

        :param position_x:
        :param position_y:
        :param color:
        :return:
        """

        line = (self.size_pixel+2)*position_x
        column = (self.size_pixel+2)*position_y

        pygame.draw.rect(self.window, color, (line, column, self.size_pixel, self.size_pixel))

    def field_draw(self):
        """

        """
        for i in range(len(self.matrix_field)):
            for j in range(len(self.matrix_field[i])):
                if self.matrix_field[i][j] == 1:
                    self.pixel_draw(j, i, self.field_color)
        pass

    def snake_parts_draw(self, position_x, position_y, snake_color):
        """

        :param position_x:
        :param position_y:
        :param snake_color:
        :return:
        """

        self.pixel_draw(position_x, position_y, snake_color)

    def fruit_draw(self, position_x, position_y, fruit_color):
        """

        :param position_x:
        :param position_y:
        :param fruit_color:
        :return:
        """

        self.pixel_draw(position_x, position_y, fruit_color)


def main():
    """

    :return:
    """
    pass


if __name__ == "__main__":
    main()
