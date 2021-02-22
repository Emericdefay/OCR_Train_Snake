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
        self.snake_move_parts = [[-1, 0], [-1, 0], [-1, 0], [-1, 0]]

        self.snake_manager()

        pass

    def snake_manager(self):
        """

        :return:
        """

        pass

    def snake_move_manager(self, movement):
        """

        :param movement:
        :return:
        """
        self.snake_move_parts.insert(0, movement)
        if len(self.snake_move_parts) > len(self.snake_coordinates):
            self.snake_move_parts.pop()

        for i in range(len(self.snake_coordinates)):
            self.snake_coordinates[i][0] = self.snake_coordinates[i][0] + self.snake_move_parts[i][0]
            self.snake_coordinates[i][1] = self.snake_coordinates[i][1] + self.snake_move_parts[i][1]

    def snake_move_forward(self):
        """

        :return:
        """
        # Left:
        if self.snake_coordinates[1][0] - self.snake_coordinates[0][0] < 0:
            self.snake_move_left()
        # Right:
        if self.snake_coordinates[1][0] - self.snake_coordinates[0][0] > 0:
            self.snake_move_right()
        # Up :
        if self.snake_coordinates[1][1] - self.snake_coordinates[0][1] < 0:
            self.snake_move_up()
        # Down :
        if self.snake_coordinates[1][1] - self.snake_coordinates[0][1] > 0:
            self.snake_move_down()

    def snake_move_left(self):
        """

        :return:
        """

        self.snake_move_manager([-1, 0])

    def snake_move_right(self):
        """

        :return:
        """

        self.snake_move_manager([1, 0])

    def snake_move_up(self):
        """

        :return:
        """

        self.snake_move_manager([0, -1])

    def snake_move_down(self):
        """

        :return:
        """

        self.snake_move_manager([0, 1])

    def snake_grow(self):
        """

        :return:
        """
        # Body -> Tail -> New_Part
        if self.snake_coordinates[-2][0] - self.snake_coordinates[-1][0] < 0:
            position_x = self.snake_coordinates[-1][0] + 1
            position_y = self.snake_coordinates[-1][1]
            self.snake_coordinates.append([position_x, position_y])

        # New_Part <- Tail <- Body
        if self.snake_coordinates[-2][0] - self.snake_coordinates[-1][0] > 0:
            position_x = self.snake_coordinates[-1][0] - 1
            position_y = self.snake_coordinates[-1][1]
            self.snake_coordinates.append([position_x, position_y])
        # Up :
        if self.snake_coordinates[-2][1] - self.snake_coordinates[-1][1] < 0:
            position_x = self.snake_coordinates[-1][0]
            position_y = self.snake_coordinates[-1][1] + 1
            self.snake_coordinates.append([position_x, position_y])
        # Down :
        if self.snake_coordinates[-2][1] - self.snake_coordinates[-1][1] > 0:
            position_x = self.snake_coordinates[-1][0]
            position_y = self.snake_coordinates[-1][1] - 1
            self.snake_coordinates.append([position_x, position_y])
        pass

    def get_snake_position(self):
        """

        :return:
        """
        return self.snake_coordinates[0]

    def fruit_manager(self):
        """

        :return:
        """
        pass

    def update(self):
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

    truc = 0

    # 4. Game manager
    while True:
        truc += 1
        # Configuration
        visual_game.clock.tick(5)
        visual_game.field_draw()

        # Fruit draw
        visual_game.fruit_draw(1, 1, model_fruit_blueberry.color)

        # Snake draw
        for snake_coordinates_x, snake_coordinates_y in control_snake.snake_coordinates:
            visual_game.snake_parts_draw(snake_coordinates_x, snake_coordinates_y, model_snake_list[0].snake_color)

        #control_snake.snake_move_forward()
        #control_snake.snake_move_up()

        #debug
        x = control_snake.get_snake_position()[0]
        y = control_snake.get_snake_position()[1]

        if truc > 4:
            control_snake.snake_grow()
            truc = 0
        control_snake.snake_move_up()

        # Update
        pygame.display.flip()


if __name__ == '__main__':
    main()