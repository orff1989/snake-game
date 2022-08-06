import pygame
from Snake import Snake
from Food import Food
from Grid import Grid


def drawGrid(surface, grid):
    if grid is not None:
        for y in range(0, int(grid.GRID_HEIGHT)):
            for x in range(0, int(grid.GRID_WIDTH)):
                if (x + y) % 2 == 0:
                    r = pygame.Rect((x * grid.GRIDSIZE, y * grid.GRIDSIZE), (grid.GRIDSIZE, grid.GRIDSIZE))
                    pygame.draw.rect(surface, (93, 216, 228), r)
                else:
                    rr = pygame.Rect((x * grid.GRIDSIZE, y * grid.GRIDSIZE), (grid.GRIDSIZE, grid.GRIDSIZE))
                    pygame.draw.rect(surface, (84, 194, 205), rr)


def game():
    grid = Grid(480, 480, 20)
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((grid.SCREEN_WIDTH, grid.SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface.convert()
    drawGrid(surface, grid)

    snake = Snake(grid)
    food = Food(grid)

    myfont = pygame.font.SysFont("monospace", 16)
    score = 0
    while (True):
        clock.tick(10)
        snake.handle_keys()
        drawGrid(surface, grid)
        snake.move()

        if snake.get_head_position() == food.position:
            snake.length += 1
            score += 1
            food.randomize_position()

        snake.draw(surface)
        food.draw(surface)

        screen.blit(surface, (0, 0))
        text = myfont.render("score {0}".format(score), 1, (0, 0, 0))
        screen.blit(text, (5, 10))
        pygame.display.update()


if __name__ == '__main__':
    game()
