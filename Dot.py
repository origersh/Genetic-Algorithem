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
        if self.isBest:
            pygame.draw.circle(self.screen, GREEN, (self.x,self.y), self.radius)
        else:
            pygame.draw.circle(self.screen, BLACK, (self.x,self.y), self.radius)
# ------------------------------------------------------------
    def move(self, maze):
        if len(self.brain.directions) > self.brain.step:
            self.acc = self.brain.directions[self.brain.step]
            self.brain.step += 1
        else: self.dead = True

        if -5 <= self.vel[0]+self.acc[0] <= 5: self.vel[0] += self.acc[0]
        if -5 <= self.vel[1]+self.acc[1] <= 5: self.vel[1] += self.acc[1]

        if self.hitMaze(maze, self.x+self.vel[0], self.y+self.vel[1]):
            self.dead = True
        else:
            self.x += self.vel[0]
            self.y += self.vel[1]
# ------------------------------------------------------------
    def update(self, maze):
        x1 = self.goal.x + self.goal.width/2
        x2 = self.x + self.radius
        y1 = self.goal.y + self.goal.height/2
        y2 = self.y + self.radius
        dis = int(math.hypot(x2 - x1, y2 - y1) / self.radius*2)

        if (not self.dead) and (not self.reachedGoal):
            self.move(maze)
            if dis < self.goal.width:
                self.reachedGoal = True
# ------------------------------------------------------------
    def calculateFintness(self):
        x1 = self.goal.x + self.goal.width/2
        x2 = self.x + self.radius
        y1 = self.goal.y + self.goal.height/2
        y2 = self.y + self.radius
        distanceToGoal = round((math.hypot(x2 - x1, y2 - y1) / self.radius*2), 3) # math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        if self.reachedGoal: self.fitness = 10000.0/(self.brain.step**2)
        else: self.fitness = 1.0/(distanceToGoal**2)
# ------------------------------------------------------------
    def giveMeBaby(self):
        baby = Dot(self.screen, self.goal)
        baby.brain = self.brain.clone()
        return baby
# ------------------------------------------------------------
    def hitMaze(self, maze, x, y):
        for rect in maze:
            if rect.left < x < rect.left+rect.width and rect.top < y < rect.top+rect.height:
                return True
        return False