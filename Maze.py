import pygame
pygame.init()

BLUE   = (0, 0, 255)

class Maze:
    def __init__(self, screen):
        self.screen = screen
        self.maze = []
        self.buildMaze()
        self.draw()
    def buildMaze(self):
        self.maze.append(pygame.Rect(0, 200, self.screen.get_width()-100, 10))
        self.maze.append(pygame.Rect(100, 400, self.screen.get_width()-100, 10))
        # Rect(left, top, width, height)
    def draw(self):
        for rect in self.maze: pygame.draw.rect(self.screen, BLUE, rect)