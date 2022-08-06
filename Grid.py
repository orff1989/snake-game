
class Grid:

    def __init__(self, screen_width, screen_height, grid_size):
        self.SCREEN_WIDTH = screen_width
        self.SCREEN_HEIGHT = screen_height
        self.GRIDSIZE = grid_size
        self.GRID_WIDTH = self.SCREEN_HEIGHT / self.GRIDSIZE
        self.GRID_HEIGHT = self.SCREEN_WIDTH / self.GRIDSIZE