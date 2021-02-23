# Libraries:
# 1. built-in modules
import sys
import random
# 2. required modules
import pygame
# 3. projects modules
import Model
import Visual


class Control:
    """

    """
    def __init__(self):
        """

        """
        self.snake_coordinates = [[16, 15], [16, 16], [17, 16], [18, 16]]
        self.snake_move_parts = [[0, -1], [-1, 0], [-1, 0], [-1, 0]]

        self.snake_tail = []
        self.fruit_position = []

        self.snake_action = False

    def snake_move_manager(self, movement):
        """

        :param movement:
        """
        self.snake_move_parts.insert(0, movement)
        if len(self.snake_move_parts) > len(self.snake_coordinates):
            self.snake_move_parts.pop()

        self.snake_tail = self.snake_coordinates[-1].copy()

        for i in range(len(self.snake_coordinates)):
            self.snake_coordinates[i][0] = self.snake_coordinates[i][0] + self.snake_move_parts[i][0]
            self.snake_coordinates[i][1] = self.snake_coordinates[i][1] + self.snake_move_parts[i][1]

    def snake_move_forward(self):
        """

        """
        # Left:
        if self.snake_coordinates[1][0] - self.snake_coordinates[0][0] > 0:
            self.snake_move_left()
        # Right:
        if self.snake_coordinates[1][0] - self.snake_coordinates[0][0] < 0:
            self.snake_move_right()
        # Up :
        if self.snake_coordinates[1][1] - self.snake_coordinates[0][1] > 0:
            self.snake_move_up()
        # Down :
        if self.snake_coordinates[1][1] - self.snake_coordinates[0][1] < 0:
            self.snake_move_down()

    def snake_move_left(self):
        """

        """
        self.snake_move_manager([-1, 0])

    def snake_move_right(self):
        """

        """
        self.snake_move_manager([1, 0])

    def snake_move_up(self):
        """

        """
        self.snake_move_manager([0, -1])

    def snake_move_down(self):
        """

        """
        self.snake_move_manager([0, 1])

    def snake_grow(self):
        """

        """
        self.snake_coordinates.append(self.snake_tail)

    def get_snake_position(self):
        """

        :return:
        """
        return self.snake_coordinates[0]

    def snake_action_done(self):
        """

        """
        self.snake_action = False

    def fruit_spawner(self):
        """

        :return:
        """
        fruit_pos_x = random.randint(0, 31)
        fruit_pos_y = random.randint(0, 31)

        for snake_pos_x, snake_pos_y in self.snake_coordinates:
            if snake_pos_x == fruit_pos_x and snake_pos_y == fruit_pos_y:
                self.fruit_spawner()

        self.fruit_position = [fruit_pos_x, fruit_pos_y]

    def die(self):
        """

        :return:
        """
        if self.get_snake_position() in self.snake_coordinates[1:]:
            return True
        if self.get_snake_position()[0] < 0 or self.get_snake_position()[0] > 31:
            return True
        if self.get_snake_position()[1] < 0 or self.get_snake_position()[1] > 31:
            return True
        return False


def start():
    """

    :return:
    """
    # Initialisation
    # 1. Game window init
    visual_game = Visual.GameWindow()
    visual_game.field_draw()
    run = True

    # 2. Fruits models init
    model_fruit_apple = Model.Fruits(0)
    model_fruit_leaf = Model.Fruits(1)
    model_fruit_blueberry = Model.Fruits(2)

    # 3. Snake init
    model_snake_list = []
    control_snake = Control()
    for i in range(len(control_snake.snake_coordinates)):
        model_snake_list.append(Model.SnakePart(i))

    # 4. Fruit init
    control_snake.fruit_spawner()

    # 5. Game runner
    while run:
        # Configuration
        visual_game.clock.tick(5)
        visual_game.field_draw()

        # Exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                sys.exit()

        # Eat event
        if control_snake.get_snake_position() == control_snake.fruit_position:
            control_snake.snake_grow()
            control_snake.fruit_spawner()

        # Keys event
        keys = pygame.key.get_pressed()

        if not control_snake.snake_action:
            if keys[pygame.K_LEFT]:
                control_snake.snake_action = True
                control_snake.snake_move_left()
            if keys[pygame.K_RIGHT]:
                control_snake.snake_action = True
                control_snake.snake_move_right()
            if keys[pygame.K_UP]:
                control_snake.snake_action = True
                control_snake.snake_move_up()
            if keys[pygame.K_DOWN]:
                control_snake.snake_action = True
                control_snake.snake_move_down()

        # Keys non-event
        if not control_snake.snake_action:
            control_snake.snake_move_forward()

        # Game lost
        if control_snake.die():
            font = pygame.font.SysFont("comicsans", 100)
            text = font.render("You died.", 1, (255, 0, 0))
            visual_game.window.blit(text, (visual_game.WIDTH//2, visual_game.HEIGHT//2))
            pygame.display.flip()
            pygame.time.wait(2000)
            start()

        # Fruit draw
        fruit_x = control_snake.fruit_position[0]
        fruit_y = control_snake.fruit_position[1]
        visual_game.fruit_draw(fruit_x, fruit_y, model_fruit_apple.color)

        # Snake draw
        for snake_coordinates_x, snake_coordinates_y in control_snake.snake_coordinates:
            visual_game.snake_parts_draw(snake_coordinates_x, snake_coordinates_y, model_snake_list[0].snake_color)

        # Move done
        control_snake.snake_action_done()

        # Update
        pygame.display.flip()


if __name__ == '__main__':
    start()
