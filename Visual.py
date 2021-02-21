import pygame


class GameWindow:
    """

    """
    WIDTH = 800
    HEIGHT = WIDTH
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

        self.lines = GameWindow.WIDTH // 100
        self.columns = GameWindow.HEIGHT // 100

        self.pixel = pygame.draw.rect(self.window, (0, 0, 0), (0, 0, 0, 0))

        self.matrix = [[1 for i in range(32)] for j in range(32)]
        self.position_x = 0
        self.position_y = 0
        pass

    def pixel_draw(self, position_x, position_y, color):
        """

        :param position_x:
        :param position_y:
        :param color:
        :return:
        """

        tuple_color = (color, color, color)

        pygame.draw.rect(self.window, tuple_color, (position_x+2, position_y+2, 21, 21))

    def field_draw(self, matrix):
        """

        :param matrix:
        :return:
        """
        position_x = 0
        position_y = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    self.pixel_draw(position_x, position_y, 10)
                    #print(i, ':', position_x, ";", j, ":", position_y)
                position_x += 25
            position_y += 25
            position_x = 0

        pass

    def snake_draw(self, position_x, position_y):
        """

        :param position_x:
        :param position_y:
        :return:
        """
        self.pixel_draw(position_x, position_y, 255)

    def update(self):
        """

        :return:
        """
        self.position_x += 100
        self.position_x % 800
        pass


def main():
    """

    :return:
    """
    a = GameWindow()
    while True:
        a.clock.tick(1)
        a.field_draw(a.matrix)
        pygame.display.flip()


if __name__ == "__main__":
    main()
