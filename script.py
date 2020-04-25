import sys, pygame, Dot, Population, Maze
pygame.init()

# ------------------------------------------------------------
RED    = (255, 0, 0)
BLACK  = (0, 0, 0)
WHITE  = (255, 255, 255)

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK  = pygame.time.Clock()

GOAL_X, GOAL_Y = int(SCREEN_WIDTH/2), 20
GOAL_RADIUS = 5
GOAL = pygame.draw.circle(SCREEN, RED, (GOAL_X, GOAL_Y), GOAL_RADIUS)

MAZE = Maze.Maze(SCREEN)
SCREEN.fill(WHITE)
WORLD = Population.Population(SCREEN, GOAL, 10)
# ------------------------------------------------------------

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    # SCREEN.fill(WHITE)
    MAZE.draw()
    pygame.draw.circle(SCREEN, RED, (GOAL_X, GOAL_Y), GOAL_RADIUS)

    if WORLD.allDotsDead():
        WORLD.calculateFitness()
        WORLD.naturalSelection()
        WORLD.mutateDemBabies()
        SCREEN.fill(WHITE)
    else:
        WORLD.update(MAZE.maze)
        WORLD.draw()
        pygame.display.update()

    CLOCK.tick(100)
print("Congradulations! You've reached generation: #{}".format(WORLD.gen))