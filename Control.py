import pygame
import Model
import Visual


class Control:
    """

    """
    def __init__(self):
        """

        """
        self.past_matrix = [[0 for i in range(32)] for j in range(32)]
        self.present_matrix = [[0 for i in range(32)] for j in range(32)]

        self.fruit_position = [5, 5]

        self.snake_coordinates = [[15, 16], [16, 16], [17, 16], [18, 16]]
        pass

    def snake_manager(self):
        """

        :return:
        """

        pass

    def snake_move_forward(self):
        """

        :return:
        """
        pass

    def snake_turn(self):
        """

        :return:
        """
        pass

    def snake_grow(self):
        """

        :return:
        """
        pass

    def fruit_manager(self):
        """

        :return:
        """
        pass


def main():
    """

    :return:
    """
    # Initialisation
    # 1. Game window
    visual_game = Visual.GameWindow()
    visual_game.field_draw()

    # 2. Fruits models
    model_fruit_apple = Model.Fruits(0)
    model_fruit_leaf = Model.Fruits(1)
    model_fruit_blueberry = Model.Fruits(2)

    # 3. Snake
    model_snake_list = []
    control_snake = Control()
    for i in range(len(control_snake.snake_coordinates)):
        model_snake_list.append(Model.SnakePart(i))

    # 4. Game manager
    while True:
        # Configuration
        visual_game.clock.tick(24)
        visual_game.field_draw()
        # Initialization
        visual_game.fruit_draw(1, 1, f2.color)
        #
        for serpents_parties in console.serpents_coord:
            visual_game.snake_parts_draw(22, 2, s.snake_color)

        # Update
        pygame.display.flip()


if __name__ == '__main__':
    main()