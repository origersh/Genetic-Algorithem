import pygame, Dot
from random import uniform
pygame.init()

class Population():
# ------------------------------------------------------------
    def __init__(self, screen, goal, size):
        self.screen = screen
        self.goal = goal
        self.size = size
        self.dots = []

        self.fitnessSum = 0.0
        self.gen = 1
        self.bestDot = 0
        self.minStep = 400

        self.first2reach = True
        
        for i in range(self.size):
            self.dots.append(Dot.Dot(self.screen, self.goal))
# ------------------------------------------------------------
    def draw(self):
        for i in range(1, self.size):   ####
            self.dots[i].draw()
        self.dots[0].draw()
# ------------------------------------------------------------
    def update(self, maze):
        for i in range(self.size):   ####
            if self.dots[i].brain.step >= self.minStep:
                self.dots[i].dead = True
            else:
                self.dots[i].update(maze)
# ------------------------------------------------------------
    def calculateFitness(self):
        for i in range(self.size):   ####
            self.dots[i].calculateFintness()
# ------------------------------------------------------------
    def allDotsDead(self):
        for i in range(self.size):   ####
            if (not self.dots[i].dead) and (not self.dots[i].reachedGoal):
                return False
        return True
# ------------------------------------------------------------
    def naturalSelection(self):
        newDots = []
        self.setBestDot()
        self.calculateFintnessSum()

        newDots.append(self.dots[self.bestDot].giveMeBaby())
        newDots[0].isBest = True

        for i in range(1, self.size):   ####
            parent = self.selectParent()
            newDots.append(parent.giveMeBaby())
        self.dots = newDots
        self.gen += 1
# ------------------------------------------------------------
    def calculateFintnessSum(self):
        self.fitnessSum = 0.0
        for i in range(self.size):  ####
            self.fitnessSum += self.dots[i].fitness
# ------------------------------------------------------------
    def selectParent(self):
        rand = uniform(0.0, self.fitnessSum)
        runningSum = 0.0
        for i in range(self.size):
            runningSum += self.dots[i].fitness
            if runningSum > rand: return self.dots[i]
        print("Error: How did you get here?")
# ------------------------------------------------------------
    def mutateDemBabies(self):  ####
        for i in range(1, self.size): self.dots[i].brain.mutate()
# ------------------------------------------------------------
    def setBestDot(self):
        m, maxIndex = 0, 0
        for i in range(self.size):  ####
            if self.dots[i].fitness > m:
                m = self.dots[i].fitness
                maxIndex = self.dots.index(self.dots[i])
        self.bestDot = maxIndex

        if self.dots[self.bestDot].reachedGoal:
            if self.first2reach:
                print(f"First generation to reach the goal: #{self.gen}")
                self.first2reach = False
            self.minStep = self.dots[self.bestDot].brain.step