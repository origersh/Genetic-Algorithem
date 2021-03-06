"""
#
# Dots: A genetic algorithem (AI) to teach my computer to solve mazes
# 
"""
import sys, pygame, Population, Maze
pygame.init()

RED    = (255, 0, 0)
BLACK  = (0, 0, 0)
WHITE  = (255, 255, 255)

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK  = pygame.time.Clock()

GOAL_X, GOAL_Y = int(SCREEN_WIDTH/2), 20
GOAL_RADIUS = 6
GOAL = pygame.draw.circle(SCREEN, RED, (GOAL_X, GOAL_Y), GOAL_RADIUS)

FONT = pygame.font.SysFont("Fixedsys", 20)

MAZE = Maze.Maze(SCREEN)
WORLD = Population.Population(SCREEN, GOAL, 400)
# SCREEN.fill(WHITE)

# ------------------------------------------------------------
while True:
    # check for user trying to exit the program - display exit message
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(f"Congradulations! You've reached generation: #{WORLD.gen}")
            sys.exit()
    
    # first inisializations
    SCREEN.fill(WHITE) # paint the screen white
    MAZE.draw() # make maze
    pygame.draw.circle(SCREEN, RED, (GOAL_X, GOAL_Y), GOAL_RADIUS) # make goal

    # make next generation when all current generation's dots are dead
    if WORLD.allDotsDead():
        WORLD.calculateFitness()
        WORLD.naturalSelection()
        WORLD.mutateDemBabies()
        # SCREEN.fill(WHITE)
    else:
        # display generation's number
        TEXT = FONT.render(f"Generation: #{WORLD.gen}", True, (0,0,0))
        SCREEN.blit(TEXT, (10, 5))

        # continue to run current generation until all dots are dead
        WORLD.update(MAZE.maze)
        WORLD.draw()
        pygame.display.update()

    # CLOCK.tick(50)    # to keep track on frame rate