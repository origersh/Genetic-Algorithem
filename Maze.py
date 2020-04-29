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
        self.maze.append(pygame.Rect(-20, 0, 25, self.screen.get_height()))
        self.maze.append(pygame.Rect(0, -20, self.screen.get_width(), 25))
        self.maze.append(pygame.Rect(0, self.screen.get_height()-5, self.screen.get_width(), 25))
        self.maze.append(pygame.Rect(self.screen.get_width()-5, 0, 25, self.screen.get_height()))
        self.maze.append(pygame.Rect(0, 100, self.screen.get_width()-100, 11))
        self.maze.append(pygame.Rect(100, 200, self.screen.get_width(), 11))
        self.maze.append(pygame.Rect(0, 300, self.screen.get_width()-100, 11))
        self.maze.append(pygame.Rect(100, 400, self.screen.get_width(), 11))
        self.maze.append(pygame.Rect(100, 400, self.screen.get_width(), 11))
    def draw(self):
        for rect in self.maze: pygame.draw.rect(self.screen, BLUE, rect)