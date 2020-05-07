import pygame, Brain, math
pygame.init()

BLACK = (0,0,0)
GREEN = (0,255,0)

class Dot:
# ------------------------------------------------------------
    def __init__(self, screen, goal):
        self.screen = screen
        self.goal = goal
        self.radius = 2
        self.x = int(self.screen.get_width()/2)
        self.y = int(self.screen.get_height()-self.radius*2-self.radius)
        self.vel = [0,0]
        self.acc = (0,0)
        
        self.brain = Brain.Brain(600)
        
        self.dead = False
        self.reachedGoal = False
        self.fitness = 0.0
        self.isBest = False
# ------------------------------------------------------------
    def draw(self):
        # draw the dot, best dot sould be green
        if self.isBest:
            pygame.draw.circle(self.screen, GREEN, (self.x,self.y), self.radius)
        else:
            pygame.draw.circle(self.screen, BLACK, (self.x,self.y), self.radius)
# ------------------------------------------------------------
    def move(self, maze):
        # move to next step, add acceleration
        if len(self.brain.directions) > self.brain.step:
            self.acc = self.brain.directions[self.brain.step]
            self.brain.step += 1
        else: self.dead = True

        # limit velocity by +-5
        if -5 <= self.vel[0]+self.acc[0] <= 5: self.vel[0] += self.acc[0]
        if -5 <= self.vel[1]+self.acc[1] <= 5: self.vel[1] += self.acc[1]

        # die if hit the maze
        if self.hitMaze(maze, self.x+self.vel[0], self.y+self.vel[1]):
            self.dead = True
        else:
            self.x += self.vel[0]
            self.y += self.vel[1]
# ------------------------------------------------------------
    def update(self, maze):
        # calculate distance from goal - to check is reached the goal
        x1 = self.goal.x + self.goal.width/2
        x2 = self.x + self.radius
        y1 = self.goal.y + self.goal.height/2
        y2 = self.y + self.radius
        dis = int(math.hypot(x2 - x1, y2 - y1) / self.radius*2)

        # check if reached the goal
        if (not self.dead) and (not self.reachedGoal):
            self.move(maze)
            if dis < self.goal.width:
                self.reachedGoal = True
# ------------------------------------------------------------
    def calculateFintness(self):
        # calculate distance from goal - to calculate fitness
        x1 = self.goal.x + self.goal.width/2
        x2 = self.x + self.radius
        y1 = self.goal.y + self.goal.height/2
        y2 = self.y + self.radius
        distanceToGoal = round((math.hypot(x2 - x1, y2 - y1) / self.radius*2), 3) # math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        # calculate fitness - if dot reached the goal its fitness should be much grater than the others
        if self.reachedGoal: self.fitness = 10000.0/(self.brain.step**2)
        else: self.fitness = 1.0/(distanceToGoal**2)
# ------------------------------------------------------------
    def giveMeBaby(self):
        # make the next generation by cloning the brain of the dot
        baby = Dot(self.screen, self.goal)
        baby.brain = self.brain.clone() # were changing the brain a little to bring progress to next generation
        return baby
# ------------------------------------------------------------
    def hitMaze(self, maze, x, y):
        # check if dot inside the maze - that's a hit
        for rect in maze:
            if rect.left < x < rect.left+rect.width and rect.top < y < rect.top+rect.height:
                return True
        return False