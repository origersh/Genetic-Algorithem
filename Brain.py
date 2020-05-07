from random import randint, uniform

class Brain:
    def __init__(self, size):
        self.directions = []
        self.step = 0
        self.size = size
        self.randomize()
    def randomize(self):
        # make the brain as a list of random directions (choose bwtween 4 basic directions)
        for i in range(self.size):
            self.directions.append((randint(-1, 1), randint(-1, 1)))
    def clone(self):
        # copy brain (directions list) to the next generation
        c = Brain(self.size)
        for i in range(c.size):
            c.directions[i] = self.directions[i]
        return c
    def mutate(self):
        # change bits of the brain to a random direction inorder to progress
        mutationRate = 0.01 # the part of the population that changes
        for i in range(self.size):
            rand = uniform(0.0,1.0)
            if rand < mutationRate:
                self.directions[i] = (randint(-1, 1), randint(-1, 1))